from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.contrib.auth import login, authenticate

from . models import Post
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

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
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
