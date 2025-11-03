from django.db import models
from user.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Build(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="builds")
    lvl1to20 = ArrayField(models.CharField(max_length=500), blank=True, default=list) #  MVP! In the future, it must contain class/subclass:abilities, feasts
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Like(models.Model):
    build = models.ForeignKey(Build, on_delete=models.CASCADE, related_name="likes")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="given_likes")

    class Meta:
        unique_together = ('build', 'author')
