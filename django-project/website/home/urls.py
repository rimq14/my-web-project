from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('home', views.FunctionsViewSet)


urlpatterns = [
    # /home/
    path('', include(router.urls)),
    # # /home/choices
    # path('menu/', views.menu, name='menu'),
    # # /home/choices/1
    # path('choice/<int:pk>', views., name='choice-detail'),
]
