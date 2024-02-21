from rest_framework import viewsets
from .models import Conversation, ConversationMessage
from .serializers import ConversationSerializer, ConversationMessageSerializer
from rest_framework import generics

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer



class ConversationListAPIView(generics.ListAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    
    
    
class ConversationMessageViewSet(viewsets.ModelViewSet):
    queryset = ConversationMessage.objects.all()
    serializer_class = ConversationMessageSerializer
    
    
class ConversationMessageListAPIView(generics.ListAPIView):
    queryset = ConversationMessage.objects.all()
    serializer_class = ConversationMessageSerializer