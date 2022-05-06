from .models import Pic, Books
from rest_framework import viewsets
from .serializer import PicSerializer
from .serializer import BooksSerializer
from rest_framework.parsers import JSONParser, MultiPartParser  # 解析器


# Create your views here.
class PicViewSet(viewsets.ModelViewSet):
    # queryset 数据库中查询出来的结果集合
    queryset = Pic.objects.all()
    serializer_class = PicSerializer
    # parser_classes = [JSONParser, MultiPartParser]
    #
    # def post(self, request):
    #     data = request.data
    #     files = request.FILES.getlist('img')
    #     for file in files:
    #         serializer = self.get_serializer(
    #             data={"img": file, "picture": data["picture"]})
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #     from rest_framework.response import Response
    #     return Response("获取成功", status=200)


class BooksViewSet(viewsets.ModelViewSet):
    # queryset 数据库中查询出来的结果集合
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
