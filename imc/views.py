from django.shortcuts import render
from .serializers import ImcSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImcSerializer

class ImcPost(APIView):
    def post(self, request, format=None):
        serializer = ImcSerializer(data=request.data)
        if serializer.is_valid():
          
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
