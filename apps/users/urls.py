from django.conf.urls import url,include
from .views import UserInfoView, UploadImageView, UpdatePwdView, SendEmailCode, UpdateEmailView, MyCourseView

urlpatterns =[
    url(r'^info/$', UserInfoView.as_view(), name= 'user_info'),
    url(r'^image/upload/$', UploadImageView.as_view(), name='image_upload'),
    # 用户中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name='update_pwd'),
    #发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCode.as_view(), name='sendemail_code'),
    # 修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name='update_email'),
    url(r'^mycourse/$', MyCourseView.as_view(), name='mycourse'),
]
