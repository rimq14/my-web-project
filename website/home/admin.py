from django.contrib import admin

# Register your models here.
from .models import Functions, Cd, Pic

# 向管理页面注册change，pic类
admin.site.register(Functions)
admin.site.register(Cd)
admin.site.register(Pic)
