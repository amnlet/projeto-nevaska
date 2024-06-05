from django.db import models as md
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Company(md.Model):
    # Nome
    company_name = md.CharField(max_length=100, null=True)
  
    # CNPJ
    
    crn_number = md.CharField(max_length=100, null=True)
    
    # Criada, Atualizada
    
    created_at = md.DateTimeField(auto_now_add=True, null=True)
    updated_at = md.DateTimeField(auto_now=True, null=True)
    
    def __str__(self) -> str:
        return self.company_name

class Supplier(md.Model):
    
    # Nome
    company_name = md.CharField(max_length=100, null=True)
  
    # Contato
    
    contact = md.CharField(max_length=50, null=True)
  
    # CNPJ
    
    crn_number = md.CharField(max_length=100, null=True)
    
    # Role
    ROLES = (
        ('VENDEDOR', 'Vendedor'),
    )
    
    role = md.CharField(max_length=100, choices=ROLES, default="VENDEDOR", null=True)
    
    
    # Criada, Atualizada
    
    created_at = md.DateTimeField(auto_now_add=True, null=True)
    updated_at = md.DateTimeField(auto_now=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.company_name} - {self.contact}"
    
    

class Budget(md.Model):
    
    # Nome do Orçamento
    
    budget_name = md.CharField(max_length=100, null=True)
    
    
    # Empresa

    company = md.ForeignKey(Company, on_delete=md.SET_NULL, null=True)
    
    # Dono do Orçamento
    
    owner = md.ForeignKey(User, null=True, on_delete=md.SET_NULL)
    
    
    # Descrição e Status do Pedido
    
    description = md.TextField(blank=True, null=True)
    
    STATUS = (
        ('ABERTO', 'Em andamento'),
        ('CANCELADO', 'Cancelado'),
        ('CONCLUIDO', 'Concluido'),
    )
    
    status_ped = md.CharField(choices=STATUS, max_length=50, default="Em andamento")
    
    # Criada, Atualizada
    
    created_at = md.DateTimeField(auto_now_add=True)
    updated_at = md.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return self.budget_name