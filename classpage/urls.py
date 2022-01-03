from django.urls import path,include
from rest_framework.routers import DefaultRouter
from classpage import views

router = DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),

    #创建课程 参数 teacher name simple_name
    path('createcourse/',views.createCourseView.as_view(),name='createcourse'),

    #创建班级 参数 name year season  couid(创建的课程id)
    path('createbanji/',views.createBanjiView.as_view(),name='createbanji'),

    #根据username获取该用户教 的课程  参数:username
    path('getbanjiList/',views.getbanjiListView.as_view(),name='getbanjiList'),

    #学生加入到班级中
    path('joinbanji/',views.joinBanjiView.as_view(),name='joinbanji'),

    #查找该学生的所有班级 参数:username
    path('getclassList/',views.getclassListView.as_view(),name='getclassList'),

    #查找某班级的所有学生
    path('getclassstudentinfo/',views.getClassStudentInfoView.as_view(),name='getclassstudentinfo'),

]