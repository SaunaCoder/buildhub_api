from rest_framework import viewsets
from .models import *
from .serializers import *
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class BuildViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Build.objects.all()
    serializer_class = BuildSerializer

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class LikeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)
    
