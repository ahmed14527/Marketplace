from django.urls import path, include
from rest_framework import routers
from .views import (CategoryViewSet, 
                    ItemViewSet,
                    ItemListAPIView,
                    CategoryListAPIView
                    )

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'item', ItemViewSet)



urlpatterns = [
    path('categories/list/',CategoryListAPIView.as_view(), name='category-list'),
    path('item/list/',ItemListAPIView.as_view(), name='product-list'),

    path('', include(router.urls)),

]
