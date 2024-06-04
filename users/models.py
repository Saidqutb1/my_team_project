from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Painting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='users_image/', blank=True, null=True, default='default_images/user_image.png')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'painting'

    def __str__(self):
        return self.title