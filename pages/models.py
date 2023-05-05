from django.contrib.auth.models import User
from django.db import models


class Public(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.TextField()

    created_at = models.DateTimeField(auto_now=True)

    user_id = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Public'
        verbose_name_plural = 'Publics'

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='Images', null=True, blank=True)
    public_id = models.ForeignKey(Public, related_name='images', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return str(self.image)
