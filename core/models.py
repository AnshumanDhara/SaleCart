from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    id_user = models.IntegerField()
    name = models.TextField(blank = True)
    profileimg = models.ImageField(upload_to = 'profile_images', default = 'blank.png')
    location = models.CharField(max_length = 100, blank = True)
    wishlist = models.TextField(blank = True)
    search_history = models.TextField(blank = True)
    
    def __str__(self):
        return self.user.username