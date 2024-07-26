"""
URL configuration for expensewebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from expense import views
from settings import views as v
from summary import views as v1


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BASE , name='base'),
    path('dashboard/', views.dashboard , name='dashboard'),
    path('signup/', views.user_signup , name='signup'),
    path('login/', views.user_login , name='login'),
    path('logout/', views.Logout , name='logout'),
    path('reset_pass/', views.reset_pass, name='reset_pass'),
    path('new_pass/<int:id>', views.new_pass, name='new_pass'),
    path('update_expense/<int:id>', views.update, name='update_expense'),
    path('delete_expense/<int:id>', views.Delete, name='delete_expense'),
    path('add_expense/', views.Add_Expense, name='add_expense'),
    path('myincome/', views.myincome, name='myincome'),
    path('update_income/<int:id>', views.updateincome, name='update_income'),
    path('delete_income/<int:id>', views.DeleteIncome, name='delete_income'),
    path('add_income/', views.Add_Income, name='add_income'),

    path('general-settings/', v.General , name='general-settings'),
    path('account/', v.Account , name='account-settings'),

    path('expense_s/', v1.Expense , name='expense-summary'),
    path('income_s/', v1.Income , name='income-summary'),
    path('expense_category_summary/', v1.expense_category_summary , name='expense_category_summary'),
    path('expense_monthly_category_summary/', v1.expense_monthly_category_summary, name='expense_monthly_category_summary'),
    path('income_category_summary/', v1.income_category_summary , name='income_category_summary'),
    path('income_monthly_category_summary/', v1.income_monthly_category_summary, name='income_monthly_category_summary'),

]
