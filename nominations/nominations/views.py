from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.contrib.auth import login, authenticate

from . models import *
from . forms import *

def form_submit(request):
	#must be logged in to submit a form
	if not request.user.is_authenticated:
		return redirect('/login/#notloggedin')
	if request.method == 'POST':
		print(request.POST)
		form = NominationsForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('/post/submit/#success')
		print(form.errors)
		return render(request, 'post_new.html', {'form': form,'fields': '__all__'})
	return render(request, 'post_new.html', {'form': NominationsForm,'fields': '__all__'})

def get_public_key(request, user_id):
	if not request.user.is_authenticated:
		return redirect('/login/#notloggedin')
	try:
		user = Profile.objects.get(user_id=user_id)
		return HttpResponse(user.public_key)
	except:
		return HttpResponse('invalid')

def get_private_key(request):
	#you can only get your own private key!
	if not request.user.is_authenticated:
		return redirect('/login/#notloggedin')
	return HttpResponse(Profile.objects.get(user_id=request.user.id).private_key)

def post_login(request):
	if not request.user.is_authenticated:
		return redirect('/login/#notloggedin')
	return render(request,'postlogin.html')

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.profile.first_name = form.cleaned_data.get('first_name')
			user.profile.last_name = form.cleaned_data.get('last_name')
			user.profile.email = form.cleaned_data.get('email')
			user.profile.public_key = form.cleaned_data.get('public_key')
			user.profile.private_key = form.cleaned_data.get('private_key')
			user.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})

class FormListView(ListView):
	model = Post
	template_name = 'home.html'

class FormDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'

class FormUpdateView(UpdateView):
	model = Post
	fields = '__all__'
	template_name = 'post_edit.html'


class FormDeleteView(DeleteView):
	model = Post
	template_name = 'post_delete.html'
	success_url = reverse_lazy('home')
