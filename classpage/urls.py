from django.urls import path,include
from rest_framework.routers import DefaultRouter
from classpage import views

router = DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    #创建课程，返回id
    path('createcourse/',views.createCourseView.as_view(),name='createcourse'),
    #创建班级,根据课程的id进行关联
    path('createbanji/',views.createBanjiView.as_view(),name='createbanji'),
    #根据username获取该用户教 的课程
    path('getbanjiList/',views.getbanjiListView.as_view(),name='getbanjiList'),
]