from django.forms import ModelForm
from . models import Post
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NominationsForm(ModelForm):
	commencement_date = forms.DateTimeField(input_formats=['%d-%m-%Y','%d/%m/%Y'])
	first_increment_date = forms.DateTimeField(input_formats=['%d-%m-%Y','%d/%m/%Y'])
	dob = forms.DateTimeField(input_formats=['%d-%m-%Y','%d/%m/%Y'])
	termination_date = forms.DateTimeField(input_formats=['%d-%m-%Y','%d/%m/%Y'])
	class Meta:
		model = Post
		fields = '__all__'

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
