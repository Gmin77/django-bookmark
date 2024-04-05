from django.urls import path, re_path
from . import views

app_name = 'blog'

urlpatterns= [
    path("", views.PostLV.as_view(), name='index'),
    path("post/", views.PostLV.as_view(), name="post_list"),
    path("post/<slug:slug>", views.PostDV.as_view(), name="post_detail"),
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name ='post_detail'),
    path('archive/', views.PostAV.as_view(), name='post_archive'),
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),
]