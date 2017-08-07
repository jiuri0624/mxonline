from django.conf.urls import url,include
from .views import UserInfoView

urlpatterns =[
    url(r'^info/$', UserInfoView.as_view(), name= 'user_info')
]
