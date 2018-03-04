from django.urls import path

from . import views

urlpatterns = [
    path('', views.FormListView.as_view(), name='home'),
    path('post/<int:pk>/', views.FormDetailView.as_view(), name='post_detail'),
    path('post/new/', views.FormCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/',
         views.FormUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/',
         views.FormDeleteView.as_view(), name='post_delete'),
]
