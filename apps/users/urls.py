from django.conf.urls import url,include
from .views import UserInfoView, UploadImageView, UpdatePwdView

urlpatterns =[
    url(r'^info/$', UserInfoView.as_view(), name= 'user_info'),
    url(r'^image/upload/$', UploadImageView.as_view(), name='image_upload'),
    # 用户中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name='update_pwd'),
]
