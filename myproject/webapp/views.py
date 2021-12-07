from decimal import Context
from django.core.checks import messages
from django.http.response import JsonResponse
from django.shortcuts import redirect, render

from django.http import HttpResponse, request
from django.utils.translation import deactivate
from rest_framework import generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import exception_handler

from webapp import models
from webapp.authentication import SessionCsrfExemptAuthentication
from .serializers import UserSerializer,DepartmentSerializer
from webapp.models import User,Department
from django.contrib.auth.hashers import make_password,check_password
from django.views.decorators.csrf import ensure_csrf_cookie

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import permissions,mixins


 
def index(request):
    return  HttpResponse("<H2>HEY! Welcome to Django!</H2>")

@ensure_csrf_cookie
def dashboard(request):
    return  HttpResponse("<H2>HEY! Welcome to Dashboard</H2>")

#----User view------#
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userList(request):
    user = models.User.objects.all()
    serializer = UserSerializer(user,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userDetail(request,pk):
    user = models.User.objects.get(id=pk)
    serializer = UserSerializer(user,many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def userCreate(request,fk):
    dept = Department.objects.get(pk=fk)
    user = User.objects.create(username=request.data.get("username"),
                                password=make_password(request.data.get("password")),
                                #password=request.data.get("password"),
                                email=request.data.get("email"),
                                department = dept)
    
    return Response("Successfully added user") 

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def userUpdate(request,pk,fk):
    dept = Department.objects.get(pk=fk)
    user = User.objects.update(username=request.data.get("username"),
                                password=make_password(request.data.get("password")),
                                email=request.data.get("email"),
                                department = dept)

    return Response("Successfully updated user")   


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def userDelete(request,pk):
    user = models.User.objects.get(id=pk)
    user.delete()

    return Response("Item successfully deleted!") 


#----Department view------#

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def departmentList(request):
    department = models.Department.objects.all()
    serializer = DepartmentSerializer(department,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def departmentDetail(request,pk):
    department = models.Department.objects.get(id=pk)
    serializer = DepartmentSerializer(department,many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def departmentCreate(request):
    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)  

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def departmentUpdate(request,pk):
    user = models.Department.objects.get(id=pk)
    serializer = DepartmentSerializer(instance =user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)  

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def departmentDelete(request,pk):
    user = models.Department.objects.get(id=pk)
    user.delete()

    return Response("Item successfully deleted!") 

    