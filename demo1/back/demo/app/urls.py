from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# 使用router来注册viewset，让urlconf自动生成
router = DefaultRouter()
router.register('pic', views.PicViewSet)
router.register('books', views.BooksViewSet)


urlpatterns = [
    path('', include(router.urls))
]
