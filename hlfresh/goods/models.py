# -*- coding: utf-8 -*-
"""
Created on 2020/11/9
@author: 安兴菊
Description: goods应用中Model的基类
"""
from django.db import models


# Create your models here.

# 商品分类
# 模型类 对应了数据库中的一张表
class GoodsCategory(models.Model):
    """商品分类模型"""
    # 分类名称  max_length 最大长度，字符串类型必须定义
    cag_name = models.CharField(max_length=30)
    # 分类样式
    cag_css = models.CharField(max_length=20)
    # 分类图片
    cag_img = models.ImageField(upload_to='cag')


# 商品表
# 模型类
class GoodsInfo(models.Model):
    # 商品名字
    goods_name = models.CharField(max_length=100)
    # 商品价格
    goods_price = models.IntegerField(default=0)
    # goods_price = models.CharField(max_length=100)
    # 商品描述
    goods_desc = models.CharField(max_length=1000)
    # 商品图片
    goods_img = models.ImageField(upload_to='goods')
    # 所属的分类（商品分类和商品表是一对多的关系）
    goods_cag = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE)
