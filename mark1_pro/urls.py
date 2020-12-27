"""mark1_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.HomePage.as_view(),name='home'),
    url(r'accounts/',include('accounts.urls',namespace='accounts')),
    url(r'accounts/',include('django.contrib.auth.urls')),
    url(r'^in/$', views.InPage.as_view(),name="in"),
    
    url(r'^out/$', views.OutPage.as_view(),name="out"),

    url(r'^posts/',include('posts.urls',namespace='posts')),
    url(r'^groups/',include('groups.urls',namespace='groups')),
    path('search',views.search,name='search'),
    path('search_group',views.search_group,name='search_group'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

