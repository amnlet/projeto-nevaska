from django.contrib import admin
from .models import User, Budget, Company, Supplier

# Register your models here.

admin.site.register(User)
admin.site.register(Budget)
admin.site.register(Company)
admin.site.register(Supplier)