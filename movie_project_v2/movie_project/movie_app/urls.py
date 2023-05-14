from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('sinemalar/', views.sinemalar, name="sinemalar"),
    path('<str:film_title>/', views.film_detail, name='film_detail'),
]
