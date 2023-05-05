from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('map/', views.map, name='map')
]
