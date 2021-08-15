from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyApp(models.Model):
    name = models.CharField(max_length=64, unique=True)
    desc = models.TextField(default='', blank=True)
    image = models.ImageField(upload_to='my_apps')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='my_apps')

    def __str__(self):
        return f'{self.id} {self.name}'

    class Meta:
        verbose_name_plural = 'my apps'
        ordering = ['name']

class Certificate(models.Model):
    name2 = models.CharField(max_length=64, unique=True)
    desc2 = models.TextField(default='', blank=True)
    image2 = models.ImageField(upload_to='certificates')
    created_at2 = models.DateTimeField(auto_now_add=True)
    created_by2 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='certificates')

    def __str__(self):
        return f'{self.id} {self.name2}'

    class Meta:
        verbose_name_plural = 'certificates'
        ordering = ['name2']

# class Contact(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#     phone = models.CharField(max_length=50)
#     message = models.TextField()
#
#     def __str__(self):
#         return self.name