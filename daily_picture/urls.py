"""daily_picture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from login import views

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^api/pictures/', include('picture.urls')),
    url(r'^auth/me', views.get_current_user),
    url(r'^auth/logout', views.logout_user),
    url(r'^auth/token', obtain_jwt_token),
    # ...
]