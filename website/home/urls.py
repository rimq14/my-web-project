from django.urls import path
from . import views

urlpatterns = [
    # /home/
    path('', views.index, name='index'),
    # # /home/choices
    # path('menu/', views.menu, name='menu'),
    # # /home/choices/1
    # path('choice/<int:pk>', views., name='choice-detail'),
]
