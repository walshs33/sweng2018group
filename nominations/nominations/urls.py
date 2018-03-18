from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.FormListView.as_view(), name='home'),
    path('post/<int:pk>/', views.FormDetailView.as_view(), name='post_detail'),
    #path('post/new/', views.FormCreateView.as_view(), name='post_new'),
	path('post/submit/',views.form_submit,name='post_new'),
	path('post/new/',views.form_submit,name='post_new'),
    #path('post/<int:pk>/edit/',
    #     views.FormUpdateView.as_view(), name='post_edit'),
    #path('post/<int:pk>/delete/',
    #     views.FormDeleteView.as_view(), name='post_delete'),
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout')
]
