from rest_framework import viewsets

from .models import Functions, Cd, Pic
from .serializers import FunctionsSerializer, CdSerializer, PicSerializer


# # Create your views here.
# def index(request):
#     return render(request, 'index.html')
#     # return HttpResponse('hello world!')
# 写入相应的视图集来处理请求
class FunctionsViewSet(viewsets.ModelViewSet):
    queryset = Functions.objects.all()
    serializer_class = FunctionsSerializer


class CdViewSet(viewsets.ModelViewSet):
    queryset = Cd.objects.all()
    serializer_class = CdSerializer


class PicViewSet(viewsets.ModelViewSet):
    queryset = Pic.objects.all()
    serializer_class = PicSerializer
