from django.conf.urls import include
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [ 
 path('webapp/', views.index),
 path('webapp/dashboard/', views.dashboard, name='dashboard'),
 #path('webapp/login/', views.login , name='login'),
 #path('accounts/', include('django.contrib.auth.urls')), # new



 #----User view------#
 path('user-list/',views.userList,name="user-list"),
 path('user-detail/<str:pk>/',views.userDetail,name="user-detail"),
 path('user-create/<str:fk>/',views.userCreate,name="user-create"),
 path('user-update/<str:pk>/<str:fk>/',views.userUpdate,name="user-update"),
 path('user-delete/<str:pk>/',views.userDelete,name="user-delete"),

 #----Department view------#
path('department-list/',views.departmentList,name="department-list"),
path('department-detail/<str:pk>/',views.departmentDetail,name="department-detail"),
 path('department-create/',views.departmentCreate,name="department-create"),
 path('department-update/<str:pk>/',views.departmentUpdate,name="department-update"),
 path('department-delete/<str:pk>/',views.departmentDelete,name="department-delete"),
]