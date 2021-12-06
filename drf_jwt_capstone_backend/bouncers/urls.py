from django.urls import path
from . import views

urlpatterns = [
    path('bouncers/', views.BouncerList.as_view()),
    path('bouncers/<int:pk>/', views.BouncerDetails.as_view())
]