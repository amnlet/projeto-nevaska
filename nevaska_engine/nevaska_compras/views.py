from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Budget, Company

# Create your views here.

def mainView(request):
    if request.user.is_authenticated:    
        title = "Grupo Nevaska"
        user = request.user
        filter_budget = Budget.objects.filter(owner=user)
        budgets = Budget.objects.all()
        context = {'title': title, 'user': user, 'filter_budget': filter_budget, 'budgets': budgets}
        res = render(request, 'main.html', context)
        return HttpResponse(res)
    else:
        return redirect('login')
    
def c_budget(request):
    companies = Company.objects.all()
    if request.method == "POST":
        budget_name = request.POST['budget_name']
        budget_company = request.POST['opt-emp']
        budget_description = request.POST['budget_desc']
        budget = Budget(budget_name=budget_name, company=budget_company, description=budget_description, owner=request.user)
        budget.save()
        return redirect('main')        
    context = {'companies':companies}
    res = render(request, 'c_budget.html', context)
    return HttpResponse(res)

# Login e Logout

def loginView(request):
    if request.method == "POST":
        username = request.POST['login']    
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, "Dados invalidos fale com seu administrador")
    else:
        res = render(request, 'login.html')
        return HttpResponse(res) 
    
            
        
def logoutView(request):
    logout(request)
    return redirect('login')

# Def de exclusoes

def deleteBudget(request, pk):
    budget = get_object_or_404(Budget, id=pk)
    if request.method == "POST":
        budget.delete()
        return redirect('main')

