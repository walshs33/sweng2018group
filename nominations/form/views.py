from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . models import Post


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
