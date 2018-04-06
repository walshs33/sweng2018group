from django.forms import ModelForm
from . models import Post
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import connection

class NominationsForm(ModelForm):
	commencement_date = forms.DateTimeField(input_formats=['%d-%m-%Y','%d/%m/%Y'])
	first_increment_date = forms.DateTimeField(input_formats=['%d-%m-%Y','%d/%m/%Y'])
	dob = forms.DateTimeField(label='Date of Birth',input_formats=['%d-%m-%Y','%d/%m/%Y'])
	termination_date = forms.DateTimeField(input_formats=['%d-%m-%Y','%d/%m/%Y'])
	is_NWA = forms.NullBooleanField(label='Should salary increase in line with National Wage Agreements')
	class Meta:
		model = Post
		fields = '__all__'

from django.utils.safestring import mark_safe
class EmptyWidget(forms.PasswordInput):
	def render(self, name, value, attrs=None):
		return mark_safe('')

class RankWidget(forms.PasswordInput):
	def render(self, name, value, attrs=None):
		#What stage of the nomination process are you:
		rank_form = '<select name="rank_id" form="signup_form"><option value="0">Please select one</option>'
		cursor = connection.cursor()
		cursor.execute("SELECT id,name FROM ranks")
		ranks = cursor.fetchall()
		for rank in ranks:
			rank_form += '<option value="%d">%s</option>' % (rank[0],rank[1])
		rank_form += '</select>'
		return mark_safe(rank_form)

class DeptWidget(forms.PasswordInput):
	def render(self, name, value, attrs=None):
		return mark_safe('<select name="dept_id" form="signup_form"><option value="0">Please select faculty first</option></select>')

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=True, help_text='Required')
	last_name = forms.CharField(max_length=30, required=True, help_text='Required')
	email = forms.EmailField(max_length=254, help_text='Required')
	public_key = forms.CharField(required=True, widget=forms.HiddenInput())
	private_key = forms.CharField(required=True, widget=forms.HiddenInput())
	rank_id = forms.IntegerField(label='What stage of the nomination process are you',widget=RankWidget)
	dept_id = forms.IntegerField(label='School/Department',widget=DeptWidget)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'public_key', 'private_key', 'rank_id','dept_id')
