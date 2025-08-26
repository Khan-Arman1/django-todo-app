from .models import Todo
from django import forms
from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TodoForm(forms.ModelForm):
    class Meta:
       model = Todo
       fields = ['todo_name','todo_text','remind_date','remind_time']

       widgets = {
           'remind_date':forms.DateInput(attrs={'type':'date'}),
           'remind_time':forms.TimeInput(attrs={'type':'time'}),
       }


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')