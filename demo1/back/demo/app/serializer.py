from rest_framework import serializers
from .models import Pic, Books


# 在下面创建序列化类
class PicSerializer(serializers.ModelSerializer):
    class Meta:
        # model指明该序列化器处理的数据字段从模型类Pic参考生成
        model = Pic
        # fields 指明该序列化器包含模型类中的哪些字段，__all__指明包含所有字段
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
