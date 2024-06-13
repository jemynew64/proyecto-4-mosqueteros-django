from django.db import models
from django.contrib.auth.models import User

# Create your models here. solo lo tengo para pruebas 
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)# esto te crea automaticamente
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")#quien lo hizo esto es una vinculacion 

    def __str__(self):
        return self.title