from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home.as_view()),
    path('add-cert', views.AddCertficateView.as_view()),
]