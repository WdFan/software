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

    path('joinbanji/',views.joinBanjiView.as_view(),name='joinbanji')
]