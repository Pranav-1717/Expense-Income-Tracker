from django.shortcuts import render # type: ignore
from expense.models import AddExpense,AddIncome
import datetime
import json
from django.http import JsonResponse # type: ignore

# Create your views here.

def Expense(request):
    return render(request , 'summary/expense_s.html')


def Income(request):
    return render(request , 'summary/income_s.html')

def expense_category_summary(request):
    todays_date = datetime.date.today()
    six_month_ago = todays_date - datetime.timedelta(days=30*6)
    expenses = AddExpense.objects.filter(user =request.user , date__gte = six_month_ago , date__lte = todays_date)
    finalrep = {}

    def get_category(expense):
        return expense.category
    category_list = list(set(map(get_category,expenses)))

    def get_expense_category_amoouont(category):
        amount = 0
        filter_by_category = expenses.filter(category=category)
        for item in filter_by_category:
            amount+=item.amount
        return amount

    for x in expenses:
        for y in category_list:
            finalrep[y] = get_expense_category_amoouont(y)

    return JsonResponse({'expense_category_data':finalrep},safe=False)


def expense_monthly_category_summary(request):
    todays_date = datetime.date.today()
    six_month_ago = todays_date - datetime.timedelta(days=30*6)
    expenses = AddExpense.objects.filter(user=request.user, date__gte=six_month_ago, date__lte=todays_date)
    
    monthly_data = {}

    for expense in expenses:
        month = expense.date.strftime('%Y-%m')
        if month not in monthly_data:
            monthly_data[month] = {}
        if expense.category not in monthly_data[month]:
            monthly_data[month][expense.category] = 0
        monthly_data[month][expense.category] += expense.amount

    response_data = {
        'monthly_data': monthly_data,
    }

    return JsonResponse(response_data, safe=False)

# ******************************************************************************************************************************

def income_category_summary(request):
    todays_date = datetime.date.today()
    six_month_ago = todays_date - datetime.timedelta(days=30*6)
    incomes = AddIncome.objects.filter(user =request.user , date__gte = six_month_ago , date__lte = todays_date)
    finalrep = {}

    def get_category(income):
        return income.category
    category_list = list(set(map(get_category,incomes)))

    def get_income_category_amoouont(category):
        amount = 0
        filter_by_category = incomes.filter(category=category)
        for item in filter_by_category:
            amount+=item.amount
        return amount

    for x in incomes:
        for y in category_list:
            finalrep[y] = get_income_category_amoouont(y)

    return JsonResponse({'income_category_data':finalrep},safe=False)


def income_monthly_category_summary(request):
    todays_date = datetime.date.today()
    six_month_ago = todays_date - datetime.timedelta(days=30*6)
    incomes = AddIncome.objects.filter(user=request.user, date__gte=six_month_ago, date__lte=todays_date)
    
    monthly_data = {}

    for income in incomes:
        month = income.date.strftime('%Y-%m')
        if month not in monthly_data:
            monthly_data[month] = {}
        if income.category not in monthly_data[month]:
            monthly_data[month][income.category] = 0
        monthly_data[month][income.category] += income.amount

    response_data = {
        'monthly_data': monthly_data,
    }

    return JsonResponse(response_data, safe=False)