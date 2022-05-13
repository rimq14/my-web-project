from django.db import models
import os
import uuid  # 使用uuid 防止图片名重复



# 提取出公共的方法pictures_directory_path获取图片后缀,使用uuid创建唯一的图片名，并保存的路径和文件名一并返回
def picture_directory_path(pic_id, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return os.path.join("pictures", filename)


# 上传用于美化展示的图片
class Pic(models.Model):
    # id django会帮我们自动填充
    img = models.FileField(null=True, upload_to=picture_directory_path, verbose_name='展示的图片')

    class Meta:
        db_table = 'picture'  # 数据库表的名称
        verbose_name = '图片'  # 设置表名的中文提示
        verbose_name_plural = verbose_name


# 上传进行功能操作的图片
class Cd_pic(models.Model):
    img = models.FileField(upload_to='change_detection/pic_path', verbose_name='用于变化检测的图片')  # 图片的上传

    class Meta:
        db_table = 'cd_img'
        verbose_name = '变化检测图片'
        verbose_name_plural = verbose_name

