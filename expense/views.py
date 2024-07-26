from django.shortcuts import render,HttpResponseRedirect,HttpResponse,redirect,get_object_or_404
from .forms import SignUp,Login,Resetpass,CustomSetPasswordForm,UpdateExpense,UpdateIncome
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from django.urls import reverse
from .models import AddExpense,AddIncome
from settings.models import UserPreference
from django.core.paginator import Paginator
import json
from django.http import JsonResponse


# Create your views here.
def BASE(request):
    return render(request , 'expense/base1.html')

def dashboard(request):
    user_preference = UserPreference.objects.filter(user=request.user).first()
    currency = user_preference.currency[:3]
    expenses = AddExpense.objects.filter(user=request.user)
    paginator = Paginator(expenses,4)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator , page_number)
    return render(request , 'Home/dashboard.html',{'expenses':expenses,'currency':currency,'page_obj':page_obj})

def user_signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            messages.success(request , 'Sign Up successfully!')
            form.save()
            return HttpResponseRedirect('/login/')
    else:
        form = SignUp()
    print(form)
    return render(request,'expense/signup.html',{'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = Login(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data.get('username')
                upass = form.cleaned_data.get('password')
               
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully!!')
                    return HttpResponseRedirect('/dashboard/')
                else:
                    if not authenticate(username=uname):
                        messages.error(request, 'Incorrect Username')
                    if not authenticate(password=upass):
                        messages.error(request, 'Incorrect Password')
        else:
            form = Login()
        return render(request, 'expense/login.html', {'form': form})
    else:
         return HttpResponseRedirect('/dashboard/')

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def new_pass(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        f = CustomSetPasswordForm(user, request.POST)
        if f.is_valid():
            f.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully.')
            return HttpResponseRedirect('/login/')
        else:
            messages.error(request, 'There was an error. Please try again.')
    else:
        f = CustomSetPasswordForm(user)
    return render(request, 'expense/new-pass.html', {'f': f})

def reset_pass(request):
    if request.method == 'POST':
        form = Resetpass(request.POST)
        if form.is_valid():
            uemail = form.cleaned_data.get('email')
            user = User.objects.filter(email=uemail).first()
            if user is not None:
                # Use 'id' as the keyword argument to match the URL pattern
                #make use of reverse to generate url pass id as kwarg
                redirect_url = reverse('new_pass', kwargs={'id': user.id})
                return redirect(redirect_url)
            else:
                messages.error(request, 'No user found with this email address.')
    else:
        form = Resetpass()
    return render(request, 'expense/reset-pass.html', {'form': form})


#add expense
def Add_Expense(request):
    if request.method == 'POST':
        fm = UpdateExpense(request.POST)
        if fm.is_valid():
            am = fm.cleaned_data['amount']
            date = fm.cleaned_data['date']
            des = fm.cleaned_data['description']
            user = request.user
            category=fm.cleaned_data['category']
            reg = AddExpense(user=user ,amount=am , date=date , description=des,category=category)
            reg.save()
            return HttpResponseRedirect('/dashboard/')
        else:
            fm = UpdateExpense()
            return render(request , 'Home/add-expense.html' , {'form':fm})
    else:
        fm = UpdateExpense()
        return render(request , 'Home/add-expense.html' , {'form':fm})
        


#UpdateExpense
def update(request , id):
    if request.method == 'POST':
        pi = AddExpense.objects.get(user=request.user,pk=id)
        form = UpdateExpense(request.POST,instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi = AddExpense.objects.get(user=request.user,pk=id)
        form = UpdateExpense(instance=pi)
    return render(request , 'Home/update.html' , {'form':form})

#delete expense
def Delete(request , id):
    if request.method == 'POST':
        pi = AddExpense.objects.get(user=request.user,pk=id)
        pi.delete()
    return HttpResponseRedirect('/dashboard/')

#searching(import json and JsonResponse)
def search(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        expense = AddExpense.objects.filter(amount_starts_with = search_str , user = request.user) | AddExpense.objects.filter(date_starts_with = search_str , user = request.user) | AddExpense.objects.filter(description_starts_with = search_str , user = request.user)
        data = expense.values()
        return JsonResponse(list(data) , safe=False)
    

# *********************************************************************************************************************************************************************************************************************************************************************************************
# *********************************************************************************************************************************************************************************************************************************************************************************************

#income
def myincome(request):
    user_preference = UserPreference.objects.filter(user=request.user).first()
    currency = user_preference.currency[:3]
    income = AddIncome.objects.filter(user=request.user)
    paginator = Paginator(income,4)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator , page_number)
    return render(request , 'Home/myincome.html',{'income':income,'currency':currency,'page_obj':page_obj})


#add income
def Add_Income(request):
    if request.method == 'POST':
        fm = UpdateIncome(request.POST)
        if fm.is_valid():
            am = fm.cleaned_data['amount']
            date = fm.cleaned_data['date']
            des = fm.cleaned_data['description']
            user = request.user
            category=fm.cleaned_data['category']
            reg = AddIncome(user=user ,amount=am , date=date , description=des,category=category)
            reg.save()
            return HttpResponseRedirect('/myincome/')
        else:
            fm = UpdateIncome()
            return render(request , 'Home/add-income.html' , {'form':fm})
    else:
        fm = UpdateIncome()
        return render(request , 'Home/add-income.html' , {'form':fm})
    

#Updateincome
def updateincome(request , id):
    if request.method == 'POST':
        pi = AddIncome.objects.get(user=request.user,pk=id)
        form = UpdateIncome(request.POST,instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi = AddIncome.objects.get(user=request.user,pk=id)
        form = UpdateIncome(instance=pi)
    return render(request , 'Home/update-income.html' , {'form':form})

#delete expense
def DeleteIncome(request , id):
    if request.method == 'POST':
        pi = AddIncome.objects.get(user=request.user,pk=id)
        pi.delete()
    return HttpResponseRedirect('/myincome/')

