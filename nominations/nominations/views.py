from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms import ModelForm

from . models import Post
from . forms import NominationsForm

def form_submit(request):
	if request.method == 'POST':
		print(request.POST)
		form = NominationsForm(data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/post/submit/#success')
		print(form.errors)
		return render(request, 'post_new.html', {'form': form,'fields': '__all__'})
	return render(request, 'post_new.html', {'form': NominationsForm,'fields': '__all__'})


class FormListView(ListView):
    model = Post
    template_name = 'home.html'


class FormDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class FormCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


class FormUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'post_edit.html'


class FormDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
