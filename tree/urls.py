from django.urls import path
from django.views.generic import RedirectView
from django.conf.urls import url
from . import views

app_name = 'tree'

urlpatterns = [

    path('create/', views.create, name='create-tree-url'),
    path('delete/', views.delete, name='delete-tree-url'),
    path('node/<department_id>/', views.node_detail,name='node'),
    path('node/<int:department_id>/modify/', views.modify_post, name='modify'),
    path('node/<int:department_id>/modify/uploadFile/', views.upload_file, name='uploadFile'),
    path('node/<int:department_id>/modify/deleteFile/<int:pk>', views.delete_file, name='delete_file'),
    path('node/<int:department_id>/download_file/<int:pk>/',views.download_file,name='download_file'),

    ]
