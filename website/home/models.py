from django.db import models


# Create your models here.
# 变化检测，目标提取，目标检测，地物分类
# Change Detection, extraction of target, target detection, classification of objects
class Functions(models.Model):
    # 训练模型
    cd  = models.ForeignKey('Cd', on_delete=models.SET_NULL, null=True)
    # eot = models.ForeignKey('Eot', on_delete=models.SET_NULL, null=True)
    # td  = models.ForeignKey('Td', on_delete=models.SET_NULL, null=True)
    # coo = models.ForeignKey('Coo', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.cd

    class Meta:
        verbose_name = '功能'
        verbose_name_plural = verbose_name

# 变化检测
class Cd(models.Model):
    # 描述文本
    cd_text = models.CharField(max_length=200)
    # 变化建筑统计
    cd_num = models.IntegerField()
    # 存储的模型文件

    # 输出的结果图片和上传的图片
    pic_out = models.ManyToManyField('Pic', related_name='pic_output', verbose_name='图片输出')
    pic_in = models.ManyToManyField('Pic', related_name='pic_input', verbose_name='图片输入')
    def __str__(self):
        # return self.pic_out, self.pic_num, self.cd_text
        return self.cd_text

    class Meta:
        verbose_name = '变化检测'
        verbose_name_plural = verbose_name


# # # 目标提取
# # class Eot(models.Model):
# #     eot_out = models
#
# # 目标检测
# class Td(models.Model):
#     # 检测相同的数量
#     td_num = models.IntegerField()
#     # 存储的模型文件
#
#     # 输出的结果图
#     td_out = models.ForeignKey(Pic, on_delete=models.SET_NULL, null=True)
#
#
# # 地物分类
# class Coo(models.Model):

# 图片
class Pic(models.Model):
    outpic = models.ImageField(height_field=1024, width_field=1024)
    inpic = models.ImageField(height_field=1024, width_field=1024)

    def __str__(self):
        return self.pic_in, self.pic_out

    class Meta:
        verbose_name = '图片操作'
        verbose_name_plural = verbose_name