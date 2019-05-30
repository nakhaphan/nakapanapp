from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('zero/', views.zero,name='zero'),
    path('parasmeter/', views.testparasmeter,name='testparasmeter'),
    path('getdata/', views.getdata,name='getdata'),
    path('testform/', views.testform,name='testform'),
    path('signup/', views.sign_up,name='sign_up'),
    path('login/', views.log_in,name='log_in'),
    path('signout/', views.sign_out,name='signout'),
    path('secrete1/', views.secrete1,name='secrete1'),
    path('secrete2/', views.secrete2,name='secrete2'),
    
]