from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from .models import CourseOrg, CityDic


class OrgListView(View):
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        hot_orgs = all_orgs.order_by('click_nums')[:3]
        all_citys = CityDic.objects.all()
        city_id = request.GET.get('city', '')
        category = request.GET.get('ct', '')
        # 按类别筛选
        if category:
            all_orgs = all_orgs.filter(category=category)
        #按城市筛选
        if city_id:
            all_orgs = all_orgs.filter(city_id = int(city_id))
        org_nums = all_orgs.count()
        #排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-stu_nums')
            elif sort == 'courses':
                all_orgs =all_orgs.order_by('-course_nums')

        #分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs,1, request=request)
        orgs = p.page(page)
        return render(request, 'org-list.html', {
            'all_orgs': orgs,
            'all_citys': all_citys,
            'org_nums':org_nums,
            'city_id':city_id,
            'category':category,
            'hot_orgs':hot_orgs,
            'sort':sort,
        })