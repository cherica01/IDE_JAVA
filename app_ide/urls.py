from django.urls import path
from . import views

urlpatterns = [
    path('', views.interface_principale, name='interface'),
    path('compiler_code/', views.compiler_code, name='compiler_code'),
]
