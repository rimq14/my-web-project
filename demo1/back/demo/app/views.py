from .models import Pic, Books
from rest_framework import viewsets
from .serializer import PicSerializer
from .serializer import BooksSerializer


# Create your views here.
class PicViewSet(viewsets.ModelViewSet):
    # queryset 数据库中查询出来的结果集合
    queryset = Pic.objects.all()
    serializer_class = PicSerializer


class BooksViewSet(viewsets.ModelViewSet):
    # queryset 数据库中查询出来的结果集合
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

