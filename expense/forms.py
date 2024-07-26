from django import forms # type: ignore
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,SetPasswordForm # type: ignore
from django.contrib.auth.models import User # type: ignore
from .models import AddExpense,AddIncome

class SignUp(UserCreationForm):
    username  = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        labels = {'email': 'Email'}



class Login(AuthenticationForm):
    username = UsernameField( widget = forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    password = forms.CharField(label = 'Password' ,widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))



class Resetpass(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg'}))
    
    class Meta:
        model = User
        fields = ['email']



class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
    )
    new_password2 = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
    )


#Update expense form
class UpdateExpense(forms.ModelForm):
    class Meta:
        model = AddExpense
        fields = ['amount' , 'date' ,'category', 'description']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': ' form-control form-control-lg '}),#django use numberinput for both int nad float there is no FloatInput
            'date':forms.DateInput(attrs={'class': ' form-control form-control-lg'}),
            'category':forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description':forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        }

#Update expense form
class UpdateIncome(forms.ModelForm):
    class Meta:
        model = AddIncome
        fields = ['amount' , 'date' ,'category', 'description']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': ' form-control form-control-lg '}),#django use numberinput for both int nad float there is no FloatInput
            'date':forms.DateInput(attrs={'class': ' form-control form-control-lg'}),
            'category':forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description':forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        }



