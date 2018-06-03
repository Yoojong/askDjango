from django.conf.urls import url
from . import views

urlpatterns =[
    url('post_list1/', views.post_list1),
    url('post_list2/', views.post_list2),
    url('post_list3/', views.post_list3),
]
