#!/usr/bin/env python

from django.contrib import admin
from .models import Department, Node ,NodeFile



@admin.register(Department)  # 注册
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent') #展示项
    list_filter = ['id', 'name', 'parent'] #右侧过滤器项
    list_display_links = ['id', 'parent'] #可以作为进入的项
    search_fields = ['name']  #用作搜索的项
    list_editable = ['name']  #可编辑（与display互斥

@admin.register(Node)  # 注册
class NodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'department', 'body')
    list_filter = ['department']
    list_display_links = ['id', ]
    search_fields = ['body']
    list_editable = ['department']

@admin.register(NodeFile)  # 注册
class NodeFileAdmin(admin.ModelAdmin):
    list_display = ('id','department', 'File_name','File')
    list_filter = ['department']
    list_display_links = ['id', 'File_name']
    search_fields = ['department']
    list_editable = ['department']