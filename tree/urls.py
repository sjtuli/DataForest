from django.urls import path
from . import views

app_name = 'tree'

urlpatterns = [

    path('create/', views.create, name='create-tree-url'),
    path('delete/', views.delete, name='delete-tree-url'),
    path('node/<department_id>/', views.node_detail,name='node'),
    path('node/<int:department_id>/modify/', views.modify_post, name='modify'),
    path('node/<int:department_id>/modify/uploadFile/', views.upload_file, name='uploadFile'),#上传文件
    path('node/<int:department_id>/modify/deleteFile/<int:pk>', views.delete_file, name='delete_file'),#删除文件
    path('node/<int:department_id>/download_file/<int:pk>/',views.download_file,name='download_file'),#下载文件

    ]
