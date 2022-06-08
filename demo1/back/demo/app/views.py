# 用来编写处理web请求的视图

from .models import Pic, Cd_pic
from rest_framework.viewsets import ModelViewSet
from .serializer import *

import os
from cv2 import cv2
import numpy as np


# 对上传的图片进行保存
def dealimage(request):
    if request.method == "POST":
        if request.FILES.get("image_url") is not None:
            image_to_read = read_image(request.FILES["image_url"])
    else:
        default["error_value"] = "发生错误"
        return JsonResponse(default)
    pic_target = '../media/change_detection/pic_target'  # 分割后的图片保存的文件夹
    # 要分割后的尺寸
    cut_width = 1024
    cut_length = 1024
    picture = cv2.imread(file)  # 读取上传的图片
    (width, length, depth) = picture.shape
    # 预处理生成0矩阵
    pic = np.zeros((cut_width, cut_length, depth))
    # 计算可以划分的横纵的个数
    num_width = int(width / cut_width)
    num_length = int(length / cut_length)
    # for循环迭代生成
    for i in range(0, num_width):
        for j in range(0, num_length):
            pic = picture[i * cut_width: (i + 1) * cut_width, j * cut_length: (j + 1) * cut_length,
                  :]  # 图片数据
            result_path = pic_target + '{}_{}.jpg'.format(i + 1, j + 1)
            cv2.imwrite(result_path, pic)
    return Response("成功", status=200)


# drf 此时自动定义了几个方法
class PicViewSet(ModelViewSet):
    queryset = Pic.objects.all()  # queryset 数据库中查询出来的结果集合
    serializer_class = PicSerializer


class CdPicViewSet(ModelViewSet):
    queryset = Cd_pic.objects.all()
    serializer_class = CdPicSerializer
