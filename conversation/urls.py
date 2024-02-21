from django.urls import path, include
from rest_framework import routers
from .views import (ConversationViewSet, 
                    ConversationMessageViewSet,
                    ConversationMessageListAPIView,
                    ConversationListAPIView
                    )

router = routers.DefaultRouter()
router.register(r'Conversation', ConversationViewSet)
router.register(r'ConversationMessage', ConversationMessageViewSet)



urlpatterns = [
    path('Conversation/list/',ConversationListAPIView.as_view(), name='Conversation-list'),
    path('ConversationMessage/list/',ConversationMessageListAPIView.as_view(), name='ConversationMessage-list'),

    path('', include(router.urls)),

]
