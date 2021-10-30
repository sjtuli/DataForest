"""LearningShare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import notifications.urls
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url, include
from django.views.generic import RedirectView
from tree.views import create
from . import settings
from django.views.static import serve

urlpatterns = [
    path('', RedirectView.as_view(url='question/question_index/1')),
    path('admin/', admin.site.urls),
    url(r'^account/', include('AccountApp.urls', namespace='account')),
    url(r'^question/', include('QuestionApp.urls', namespace='question')),
    url(r'^answer/', include('AnswerApp.urls', namespace='answer')),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('notice/', include('notice.urls', namespace='notice')),
    path('tree/', include('tree.urls', namespace='tree')),
    re_path(r'media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    url(r'mdeditor/', include('mdeditor.urls')),

]
