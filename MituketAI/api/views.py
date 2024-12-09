from rest_framework import viewsets
from .models import Item, Register, Result
from .serializers import ItemSerializer, RegisterSerializer, ResultSerializer
from rest_framework.filters import SearchFilter

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (SearchFilter,)  # 修正: filter_backends
    search_fields = ('name', 'place')  # 検索対象のフィールドを指定

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class RegisterRankingViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all().order_by('-point')  # pointで降順に並べ替え
    serializer_class = RegisterSerializer

class RegisterResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
