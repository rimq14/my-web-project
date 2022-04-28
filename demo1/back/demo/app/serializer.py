from rest_framework import serializers
from .models import Pic, Books


# 在下面创建序列化类
class PicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pic
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
