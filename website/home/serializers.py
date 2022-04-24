from rest_framework import serializers

from .models import Functions, Cd, Pic


# 序列化器
class FunctionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Functions
        fields = '__all__'


class CdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cd
        fields = '__all__'


class PicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pic
        fields = '__all__'
