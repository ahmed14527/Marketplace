from rest_framework import viewsets
from .models import Category,Item
from .serializers import CatecorySerilaizer,ItemSerializer
from rest_framework.permissions import IsAdminUser
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework import generics




class CategoryViewSet(viewsets.ModelViewSet):
    
    queryset=Category.objects.all()
    serializer_class=CatecorySerilaizer
    
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CatecorySerilaizer
   
class ItemViewSet(viewsets.ModelViewSet):
    
    queryset=Item.objects.all()
    serializer_class=ItemSerializer
    
    
class ItemListAPIView(generics.ListAPIView):  
    queryset = Item.objects.all()
    serializer_class = ItemSerializer