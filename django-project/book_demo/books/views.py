from .models import Books
from rest_framework import viewsets
from .serializer import BooksSerializer


# Create your views here.
class BooksViewSet(viewsets.ModelViewSet):
    # queryset 数据库中查询出来的结果集合
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
