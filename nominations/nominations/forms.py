from django.forms import ModelForm
from . models import Post
from django import forms

class NominationsForm(ModelForm):
	commencement_date = forms.DateTimeField(input_formats=['%d-%m-%Y','%d/%m/%Y'])
	first_increment_date = forms.DateTimeField(input_formats=['%d-%m-%Y','%d/%m/%Y'])
	dob = forms.DateTimeField(input_formats=['%d-%m-%Y','%d/%m/%Y'])
	termination_date = forms.DateTimeField(input_formats=['%d-%m-%Y','%d/%m/%Y'])
	class Meta:
		model = Post
		fields = '__all__'
