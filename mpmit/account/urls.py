from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


from .import views

urlpatterns = [
    path('register', views.register,name="register"),
    path('signin', views.signin,name="signin"),
    path('logout', views.logout,name="logout"),
    path('addstudentData', views.addstudentData,name="addstudentData"),
    path('viewstudentData', views.viewstudentData, name="viewstudentData"),
    path('studentdelete/<int:id>', views.viewstudentDelete, name="viewstudentDelete"),
    path('studentedit/<int:id>', views.studentEdit, name="studentEdit"),
    path('studentupdate/<int:id>', views.studentupdate, name="studentupdate"),



]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)