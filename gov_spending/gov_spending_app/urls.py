from django.urls import path

# import the views in application
from . import views

urlpatterns = [
    path('', views.index)
]
