from .models import Pic, Cd_pic, Split_image
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializer import *

from PIL import Image
from cv2 import cv2
import numpy as np

import os.path
import os


# drf 此时自动定义了几个方法
class PicViewSet(ModelViewSet):
    """
    允许用户查看或编辑的api路径
    """
    queryset = Pic.objects.all().order_by("-id")  # queryset 数据库中查询出来的结果集合,并倒序排序
    serializer_class = PicSerializer

    @action(methods=['get'], detail=False)
    def deal(self, request):
        data = Pic.objects.last()       # 获取数据库最后一条数据
        image = data.image_url
        a = Image.open(image)       # 打开图像
        pic_path = 'E:/web-development/web-project/demo1/back/demo/media/change_detection/pic_path/' + 'test.{}'.format(a.format.lower())  # 需要拆分图片存放文件夹
        pic_target = "E:/web-development/web-project/demo1/back/demo/media/split_images/"  # 分割后的图片保存的文件夹
        # 判断获取的图片的格式是否为opencv
        if isinstance(image, np.ndarray):
            cv2.imwrite(pic_path, image)
        else:
            # img = Image.open(image)  # 打开图像
            image = cv2.cvtColor(np.asarray(a), cv2.COLOR_RGB2BGR)
            cv2.imwrite(pic_path, image)
        # 要分割后的尺寸
        cut_width = 1024
        cut_length = 1024
        picture = cv2.imread(pic_path)      # 读取要获取的图片
        (width, length, depth) = picture.shape
        # 预处理生成0矩阵
        pic = np.zeros((cut_width, cut_length, depth))
        # 计算可以划分的横纵的个数
        num_width = int(width / cut_width)
        num_length = int(length / cut_length)
        # for循环迭代生成
        for i in range(0, num_width):
            for j in range(0, num_length):
                pic = picture[i * cut_width: (i + 1) * cut_width, j * cut_length: (j + 1) * cut_length, :]  # 图片数据
                result_path = pic_target + '{}_{}.{}'.format(i + 1, j + 1, a.format.lower())
                cv2.imwrite(result_path, pic)

        # 将拆分后的图片保存至数据库
        for filename in os.listdir(r'E:\web-development\web-project\demo1\back\demo\media\split_images'):
            s1 = Split_image(image_url="/split_images/{}".format(filename))
            s1.save()

        return Response("拆分成功", status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def fetch(self, request):
        data = request.data.get()       # 获取请求的坐标参数
        image_data = Pic.objects.last()       # 获取数据库最后一条数据
        image = image_data.image_url
        a = Image.open(image)   # 打开图片
        out_file_name = 'input'     # 输出图片的名称
        im = cv2.imread(image)
        im = im[data.y:data.y, data.x:data.x]   # 根据鼠标落下和弹起的坐标读取数据
        save_path = r"../media/change_detection/input_pic/"
        save_path_file = os.path.join(save_path,out_file_name+'.{}'.format(a.format.lower()))
        cv2.imwrite(save_path_file, im)
        return Response("框选成功",status=status.HTTP_200_OK)

class CdPicViewSet(ModelViewSet):
    queryset = Cd_pic.objects.all()
    serializer_class = CdPicSerializer

class SplitImagesViewSet(ModelViewSet):
    queryset = Split_image.objects.all()
    serializer_class = SplitImageSerializer