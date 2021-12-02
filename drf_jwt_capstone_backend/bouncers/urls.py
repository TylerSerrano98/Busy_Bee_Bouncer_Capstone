from django.urls import path
from . import views

urlpatterns = [
    path('Inflatables/', views.Bouncer.as_view()),
]