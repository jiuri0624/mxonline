from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.
from .models import CourseOrg, CityDic


class OrgListView(View):
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        org_nums = all_orgs.count()
        all_citys = CityDic.objects.all()
        return render(request, 'org-list.html', {'all_orgs': all_orgs, 'all_citys': all_citys, 'org_nums':org_nums})