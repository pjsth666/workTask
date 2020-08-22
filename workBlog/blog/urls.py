from django.urls import path
from .views import (home_blog_list, 
                    home_blog_detail,
                    work_blog_list,
                    work_blog_detail)


urlpatterns = [
    path('home_blog_list/', home_blog_list, name='home_blog_list'),
    path('home_blog_detail/<int:pk>/', home_blog_detail, name='home_blog_detail'),
    path('work_blog_list/', work_blog_list, name='work_blog_list'),
    path('work_blog_detail/<int:pk>/', work_blog_detail, name='work_blog_detail'),
]