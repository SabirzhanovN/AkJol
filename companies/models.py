from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='companies')

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)

    image_main = models.ImageField(upload_to='news')
    image_1 = models.ImageField(upload_to='news', null=True, blank=True)
    image_2 = models.ImageField(upload_to='news', null=True, blank=True)

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
