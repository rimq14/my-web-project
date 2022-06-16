from django.db import models
import os
import uuid  # 使用uuid 防止图片名重复

# 提取出公共的方法pictures_directory_path获取图片后缀,使用uuid创建唯一的图片名，并保存的路径和文件名一并返回
def picture_directory_path(pic_id, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return os.path.join("pictures", filename)

# 上传用于示例的图片
class Pic(models.Model):
    name = models.CharField(max_length=150, verbose_name="名称")      # 上传的遥感图片的地理位置名称
    image_url = models.ImageField(upload_to=picture_directory_path, verbose_name="图片")     # 图片上传
    upload_date = models.DateTimeField(auto_now_add=True)      # 图片上传的时间

    # 表信息声明
    class Meta:
        ordering = ('-upload_date',)    # 上传时间排序
        db_table = 'upload_images'  # 数据库表的名称
        verbose_name = '上传的图片'  # 设置表名的中文提示
        verbose_name_plural = verbose_name

# 上传进行功能操作的图片
class Cd_pic(models.Model):
    image_url = models.ImageField(upload_to='change_detection/pic_path', verbose_name="图片")  # 图片的上传
    class Meta:
        db_table = 'change_detection_images'
        verbose_name = '变化检测的图片'
        verbose_name_plural = verbose_name

class Split_image(models.Model):
    image_url = models.ImageField(upload_to='split_images', verbose_name="图片")
    # name = models.ForeignKey(to='Pic', on_delete=models.CASCADE)       # 一对多外键设置
    name = models.CharField(max_length=150,verbose_name="名称")
    class Meta:
        db_table = "split_images"
        verbose_name = "拆分后的图片块"
        verbose_name_plural = verbose_name
