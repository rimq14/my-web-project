from django.db import models


# Create your models here.
class Pic(models.Model):
    img = models.ImageField('图片', upload_to='pic/')

    def __str__(self):
        return self.img

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = verbose_name


class Books(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30, blank=True, null=True)
