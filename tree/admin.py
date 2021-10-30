#!/usr/bin/env python

from django.contrib import admin
from .models import Department, Node ,NodeFile

admin.site.register(Department)

admin.site.register(Node)

admin.site.register(NodeFile)