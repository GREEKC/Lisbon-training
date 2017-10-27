## Author: Aziz Khan
## License: GPL v3
## Copyright 2017 Aziz Khan <azez.khan__AT__gmail.com>

"""remap URL Configuration

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

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='ReMap REST Live API')

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('restapi.v1.urls', namespace='v1')),
    #url(r'^api/current/', include('restapi.v1.urls', namespace='current')),
    url(r'^$', schema_view),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/live/', schema_view),
]
