from django.conf.urls import url,include
from .views import UserInfoView, UploadImageView, UpdatePwdView, SendEmailCode, UpdateEmailView, MyCourseView
from .views import MyFavOrgView, MyFavTeacherView, MyFavCourseView, MyMessageView
urlpatterns =[
    url(r'^info/$', UserInfoView.as_view(), name= 'user_info'),
    url(r'^image/upload/$', UploadImageView.as_view(), name='image_upload'),
    # 用户中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name='update_pwd'),
    #发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCode.as_view(), name='sendemail_code'),
    # 修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name='update_email'),
    # 我学习的课程
    url(r'^mycourse/$', MyCourseView.as_view(), name='mycourse'),

    # 我收藏的课程机构
    url(r'^myfav/org/$', MyFavOrgView.as_view(), name='myfav_org'),
    # 我收藏的教师
    url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name='myfav_teacher'),
    # 我收藏的课程
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name='myfav_course'),

    # 我的消息
    url(r'^message/$', MyMessageView.as_view(), name='message'),
]
