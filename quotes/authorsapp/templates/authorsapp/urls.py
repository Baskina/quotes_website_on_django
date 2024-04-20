from django.urls import path
from . import views

app_name = 'authorsapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('add-author/', views.addAuthor, name='add-author'),
]
