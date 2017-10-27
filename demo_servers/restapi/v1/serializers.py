# -*- coding: utf-8 -*-
## Author: Aziz Khan
## License: GPL v3
## Copyright © 2017 Aziz Khan <azez.khan__AT__gmail.com>

from rest_framework import serializers
from .models import Tf, Gse, Ct

from django.http import HttpRequest


class TfSerializer(serializers.HyperlinkedModelSerializer):
	
	#url = serializers.HyperlinkedIdentityField(view_name="tf-detail")
	url = serializers.SerializerMethodField()

	class Meta:
		model = Tf
		fields = '__all__'
		#fields = ('url', 'transcription_factor')

	def get_url(self, obj):

		host_name = self.context['request'].build_absolute_uri(location='/')
		
		return  str(host_name)+'api/v1/tf/'+obj.transcription_factor

class GseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gse
        fields = '__all__'

class CtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ct
        fields = '__all__'

