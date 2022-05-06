from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# 使用router来注册viewset，让urlconf自动生成
router = DefaultRouter()        # 可以处理视图的路由器
router.register('pic', views.PicViewSet)    # 向路由器中注册视图集
router.register('books', views.BooksViewSet)


urlpatterns = [
    path('', include(router.urls))  # 将路由器中的所有路由信息追加到django的路由列表中
]
