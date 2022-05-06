from django.db import models
import os
import uuid     # 使用uuid 防止图片名重复

#提取出公共的方法pictures_directory_path获取图片后缀
# 使用uuid创建唯一的图片名，并保存的路径和文件名一并返回
def picture_directory_path(pic_id, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return os.path.join("pictures", filename)

# Create your models here.
class Pic(models.Model):

    # 字段映射
    # id django会帮我们自动填充
    img = models.FileField( blank=True, null=True,upload_to=picture_directory_path, verbose_name='图片')

    class Meta:
        db_table = 'picture'
        # 设置表名的中文提示
        verbose_name = '图片'
        verbose_name_plural = verbose_name



class Books(models.Model):
    name = models.CharField(max_length=30, verbose_name='书名')
    author = models.CharField(max_length=30, blank=True, null=True, verbose_name='作者')

    class Meta:
        db_table = 'books'
        verbose_name = '书本'
        verbose_name_plural = verbose_name
