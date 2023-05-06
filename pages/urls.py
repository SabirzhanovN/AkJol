from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('mapping/', views.mapping, name='mapping'),
    path('add_like/<int:id>/', views.add_like, name='add_like')
]
