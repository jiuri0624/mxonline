
from django.conf.urls import url, include
from .views import OrgListView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, AddFavView, TeacherListView, TeacherDetailView

urlpatterns = [
    # 课程机构
    url(r'^list/$', OrgListView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),
    url(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name='course'),
    url(r'^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name='desc'),
    url(r'^teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name='teacher'),
    #教师列表
    url(r'^teacher/list/$', TeacherListView.as_view(), name='teacher_list'),
    #教师详情
    url(r'^teacher/detail/(?P<teacher_id>\d+)/$', TeacherDetailView.as_view(), name='teacher_detail'),

    #机构收藏
    url(r'^add_fav/$', AddFavView.as_view(), name='add_ask'),
]