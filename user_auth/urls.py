
from django.urls import path
from .views import *
urlpatterns = [
      path('',home,name='home-page'),
      path('signup',signup,name='signup_page'),
      path('login',userlogin,name='login_page'),
      path('logout',userlogout,name='logout_page'),
      path('homepage',homes,name='homepage'),
      path('task_l',task_list,name='t_list'),
      path('delete_task/<int:id>',deleted_task, name='delete_task'),

]
