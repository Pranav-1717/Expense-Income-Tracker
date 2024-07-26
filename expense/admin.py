from django.contrib import admin  # type: ignore
from .models import AddExpense,AddIncome

# Register your models here.
@admin.register(AddExpense)
class Add_Expense(admin.ModelAdmin):
    list_display = ['user','amount','category','description','date']

@admin.register(AddIncome)
class Add_Expense(admin.ModelAdmin):
    list_display = ['user','amount','category','description','date']
