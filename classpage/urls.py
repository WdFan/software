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

    #返回FaceBase.db的数据
    path('getdbinfo/',views.getdbinfo.as_view(),name='getdbinfo'),

    #修改课程信息
    path('editLesson/',views.editLessonView.as_view(),name='editLesson'),

    #存储个人信息
    path('savePersonInfo/',views.savePersonInfoView.as_view(),name = "savePersonInfo"),

    #编辑班级信息 put请求
    path('editClass/',views.editClassView.as_view(),name="editClass"),

    #得到班级信息
    path('getClassInfo/',views.getClassInfoView.as_view(),name="getClassInfo"),

    #退出班级
    path('quitClass/',views.quitClass.as_view(),name="quitClass"),

    #删除班级
    path('deleteClass/',views.deleteClassView.as_view(),name="deleteClass"),

    # 删除课程
    path('deleteLesson/', views.deleteLesson.as_view(), name="deleteLesson"),

    #获取信息
    path('getClassMessage/', views.getClassMessageView.as_view(), name="getClassMessage"),
]