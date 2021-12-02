from django.shortcuts import render

from drf_jwt_capstone_backend.bouncers.models import Bouncer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.response import Http404
from .serializers import BouncerSerializer
# Create your views here.

class BouncerList(APIView):

    def get(self, request):
        Bouncer.objects.all()
        serializer = BouncerSerializer(bouncer, many=True)
        return Response(serializer.data)