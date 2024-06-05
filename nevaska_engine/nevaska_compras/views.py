from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Budget
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
        return render(request, 'login.html')
    
            
        
def logoutView(request):
    logout(request)
    return redirect('login')

# Def de exclusoes

def deleteBudget(request, pk):
    budget = get_object_or_404(Budget, id=pk)
    if request.method == "POST":
        budget.delete()
        return redirect('main')

