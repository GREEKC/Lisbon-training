# -*- coding: utf-8 -*-
## Author: Aziz Khan
## License: GPL v3
## Copyright © 2017 Aziz Khan <azez.khan__AT__gmail.com>

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.cache import cache_page

from . import views

#cache timeout in seconds

CACHE_TIMEOUT = 60 * 60  #24 hours
#CACHE_TIMEOUT = 0


urlpatterns = [
	#url(r'^$', cache_page(CACHE_TIMEOUT)(views.APIRoot.as_view()), name='api-root'),
	url(r'^$', views.APIRoot.as_view(), name='api-root'),

    url(r'^tf/?$', views.TfListViewSet.as_view(), name='tf-list'),
    url(r'^tf/(?P<tf_name>.+)/$', views.TfDetailsViewSet.as_view(), name='tf-detail'),

    #url(r'^home/?$', views.api_homepage, name='api-homepage'),
    #url(r'^docs/?$', views.api_docs, name='api-docs'),
    #url(r'^overview/?$', views.api_overview, name='api-overview'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json','jsonp','bed','yaml','api'])