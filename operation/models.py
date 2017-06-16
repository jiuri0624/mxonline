# -*- coding:utf-8 -*-

from django.db import models

# Create your models here.


class UserAsk(models.Model):
    pass

    class Meta:
        verbose_name = u'用户咨询'
        verbose_name_plural = verbose_name


class UserAsk(models.Model):
    pass

    class Meta:
        verbose_name = u'用户咨询'
        verbose_name_plural = verbose_name



class CourseComments(models.Model):
    pass

    class Meta:
        verbose_name = u'课程评论'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    pass

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    pass

    class Meta:
        verbose_name = u'用户消息'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    pass

    class Meta:
        verbose_name = u'学习课程'
        verbose_name_plural = verbose_name
