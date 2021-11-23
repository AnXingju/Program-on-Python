# -*- coding: utf-8 -*-
"""
Created on 2020/11/10
@author: 安兴菊
Description: goods应用中Model类注册
"""

from django.contrib import admin

from goods.models import GoodsCategory, GoodsInfo

# Register your models here.
admin.site.register([GoodsCategory, GoodsInfo])
