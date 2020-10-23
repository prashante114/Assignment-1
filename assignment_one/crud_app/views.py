from django.shortcuts import render

# Create your views here.
from crud_app.models import RouterProperties
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from . import serializers

class RouterViewset(viewsets.ModelViewSet):
    queryset = RouterProperties.objects.all()
    serializer_class = serializers.RouterPropertiesSerializer
    