# -*- coding: utf-8 -*-
"""
Created on 2020/11/10
@author: 安兴菊
Description: goods应用中views
"""

from django.shortcuts import render

from goods.models import GoodsCategory, GoodsInfo


# Create your views here.

def index(request):
    """首页页面"""
    categories = GoodsCategory.objects.all()  # 查询商品分类
    # categories 为各个商品分类信息  QuerySet类型
    for cag in categories:
        # 从每个分类中获取最后四个商品，作为最新商品数据
        # order_by 是排序 这里是根据id反向排序  从大到小  [:4]切片是获取结果集中的前4个
        # 一对多关系，查询多的一方 会在一的一方有一个属性 多的一方 模型类名小写_set
        # cag 会商品分类对象
        cag.goods_list = cag.goodsinfo_set.order_by('-id')[:4]

    # 读取购物车商品列表
    cart_goods_list = []
    # 商品总数
    cart_goods_count = 0
    for goods_id, goods_num in request.COOKIES.items():
        # 商品ID都为数字, 非数字的cookie过滤掉
        if not goods_id.isdigit():
            continue
        # 具体的商品
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        # 购买数量
        cart_goods.goods_num = goods_num
        # 显示
        cart_goods_list.append(cart_goods)
        # 累加购物车商品总数
        cart_goods_count = cart_goods_count + int(goods_num)
    return render(request, 'index.html', {'categories': categories,
                                          'cart_goods_list': cart_goods_list,
                                          'cart_goods_count': cart_goods_count})
