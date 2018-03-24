from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from project.api.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows users to be views or edited.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

