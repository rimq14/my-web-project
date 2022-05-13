from .models import Pic, Cd_pic
from rest_framework import viewsets
from .serializer import PicSerializer, CdPicSerializer


# from rest_framework.parsers import JSONParser, MultiPartParser  # 解析器
class PicViewSet(viewsets.ModelViewSet):
    # queryset 数据库中查询出来的结果集合
    queryset = Pic.objects.all()
    serializer_class = PicSerializer


class CdPicViewSet(viewsets.ModelViewSet):
    queryset = Cd_pic.objects.all()
    serializer_class = CdPicSerializer
