from django.urls import path
from twitteruser import views

urlpatterns = [
    path('regester/', views.regesterview, name='regester')
]