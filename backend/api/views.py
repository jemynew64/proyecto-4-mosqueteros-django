from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer,NoteSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from .models import Note
# Create your views here.

#solo es un ejemplo para ver si funciona hacerlo con viewsets
class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    #quienes tiene permiso para hacer esto de aca 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
