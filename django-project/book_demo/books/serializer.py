from rest_framework import serializers
from .models import Books


# 在下面创建序列化类(与django form相似)
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
