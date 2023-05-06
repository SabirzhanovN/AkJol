from django.contrib.auth.models import User
from django.db import models

from pages.models import Public


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.ForeignKey(Public, on_delete=models.CASCADE)

    review = models.CharField(max_length=500)
    list_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'



