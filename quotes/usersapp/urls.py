from django.urls import path, include
from . import views

app_name = 'usersapp'

urlpatterns = [
    path('', include('quotesapp.templates.quotesapp.urls')),
]