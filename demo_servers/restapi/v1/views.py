# -*- coding: utf-8 -*-
## Author: Aziz Khan
## License: GPL v3
## Copyright © 2017 Aziz Khan <azez.khan__AT__gmail.com>
import os
from remap.settings import BASE_DIR
from .models import Tf, Gse, Ct
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.reverse import reverse
from django.db.models import Q, Max
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.throttling import UserRateThrottle

from rest_framework import renderers

from rest_framework_jsonp.renderers import JSONPRenderer
from rest_framework_yaml.renderers import YAMLRenderer
from rest_framework_yaml.parsers import YAMLParser

from rest_framework.response import Response
from .serializers import CtSerializer, GseSerializer, TfSerializer

from rest_framework.pagination import (
    PageNumberPagination,
    )
from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView, 
    )
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
    BaseFilterBackend,
    DjangoFilterBackend,
    )
import coreapi

class TfResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


def _get_sites_fasta_url(request, base_id, version):

    if os.path.isfile(BASE_DIR+'/download/sites/'+base_id+'.'+str(version)+'.sites'):
        host_name = request.build_absolute_uri(location='/')
        return  str(host_name)+'download/sites/'+base_id+'.'+str(version)+'.sites'
    else:
        return None


class BEDListRenderer(renderers.BaseRenderer):
    '''
    Render a list of sites in BED format.
    '''
    media_type = 'text/bed'
    format = 'bed'

    def render(self, data, media_type=None, renderer_context=None):

        bed = []
        import json
        for site in data['sites']:
            region = '\t'.join([site.get('chrom'), str(site.get('start')), site.get('end'), site.get('name'), '.', site.get('strand')+"\n"])
            bed.append(region)
        
        if not bed:
            bed = 'No BED available'
            return bed
        else:
            return bed


class TfDetailsViewSet(APIView):
    """
    API endpoint that returns the TF detail information.
    """
    
    serializer_class = TfSerializer

    parser_classes = (YAMLParser,)
    renderer_classes = [renderers.JSONRenderer, JSONPRenderer, YAMLRenderer, renderers.BrowsableAPIRenderer]

    def get(self, request, tf_name, format=None):
        """
        Gets TF detail information
        """        

        data_dict = {}
        #get tf object
        tf = Tf.objects.filter(transcription_factor=tf_name).values()[0]

        data_dict = {'tf': tf}


        gses = Gse.objects.filter(transcription_factor=tf_name)
        
        gse_list = []
        for gse in gses:
            gse_list.append(gse.transcription_factor)
                    
        data_dict.update({'gse': gse_list})

    	#serializer = TfSerializer(tf, context={'request': request})
        
        return Response(data_dict)

class TfListViewSet(ListAPIView):
    """
    REST API endpoint that returns a list of all TFs.
    """
    
    serializer_class = TfSerializer
    pagination_class = TfResultsSetPagination
    throttle_classes = (UserRateThrottle,)
    filter_backends = [SearchFilter, OrderingFilter, ]
    #search_fileds = ['base_id', 'collection','name','version',]
    #filter_fileds = ['base_id', 'collection','name', 'version',]
    parser_classes = (YAMLParser,)
    renderer_classes = [ renderers.JSONRenderer, JSONPRenderer, YAMLRenderer, renderers.BrowsableAPIRenderer]

    def get_queryset(self):
        """
        List all matrix profiles
        """

        setattr(self.request, 'view', 'api-browsable')
        
        queryset = Tf.objects.all()

        return queryset


class APIRoot(APIView):
    """
    The root of the ReMap RESTful API v1.
    """

    permission_classes = (AllowAny,)

    def get(self, request, format=format):
        setattr(request, 'view', 'api-browsable')
        return Response({
            'tf': reverse('v1:tf-list', request=request),
            #'tf_detail': reverse('v1:tf-detail', request=request),
        })

def api_homepage(request):

    setattr(request, 'view', 'api-home')
    
    setattr(request, 'get_api_host', _get_api_root_url(request))
    setattr(request, 'get_host', _get_host_name(request))

    return render(request, 'rest_framework/api_home.html')

def api_docs(request):

    setattr(request, 'view', 'apidocs')
    setattr(request, 'get_api_host', _get_api_root_url(request))
    setattr(request, 'get_host', _get_host_name(request))

    return render(request, 'rest_framework/api_docs.html')

def api_overview(request):

    setattr(request, 'view', 'overview')
    setattr(request, 'get_api_host', _get_api_root_url(request))
    setattr(request, 'get_host', _get_host_name(request))

    return render(request, 'rest_framework/api_overview.html')

def api_clients(request):

    setattr(request, 'view', 'clients')
    setattr(request, 'get_api_host', _get_api_root_url(request))
    setattr(request, 'get_host', _get_host_name(request))

    return render(request, 'rest_framework/api_clients.html')


def _get_api_root_url(request):
    return request.build_absolute_uri(location='/')+'api/v1/'

def _get_host_name(request):
    return request.build_absolute_uri(location='/')


    

