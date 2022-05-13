from rest_framework import serializers
from .models import Pic, Cd_pic
from cv2 import cv2  # 进行图像拆分
import numpy as np

# 在下面创建序列化类
class PicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pic  # model指明该序列化器处理的数据字段从模型类Pic参考生成
        fields = '__all__'  # fields 指明该序列化器包含模型类中的哪些字段，__all__指明包含所有字段


# 变化检测图片
class CdPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cd_pic
        fields = '__all__'
