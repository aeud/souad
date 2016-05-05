"""souad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

# Call the views from blog app
from blog import views as blog_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', blog_views.home, name='home'),
    url(r'^new$', blog_views.new, name='blog_new'),
    url(r'^create$', blog_views.create, name='blog_post'),
    url(r'^show/(?P<article_id>\d+)$', blog_views.show, name='blog_show'),
    url(r'^edit/(?P<article_id>\d+)$', blog_views.edit, name='blog_edit'),
    url(r'^update/(?P<article_id>\d+)$', blog_views.update, name='blog_update'),
]
