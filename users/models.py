# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default='')
    birday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(choices=(('male', u'男'),('female', u'女')), max_length=6, verbose_name=u'昵称', default='female')
    address = models.CharField(max_length=10, verbose_name=u'地址', default='')
    mobile = models.CharField(max_length=11,null=True, blank=True, verbose_name=u'昵称')
    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username