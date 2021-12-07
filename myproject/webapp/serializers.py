from re import T
from django.db.models import fields
from rest_framework import serializers
from django.db import models
from django.db import IntegrityError
from rest_framework.fields import ReadOnlyField


from webapp.models import Department, User

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'code',
            'description',
        )
        model =Department

class UserSerializer(serializers.ModelSerializer):
   # department = DepartmentSerializer(many=True,read_only=True)

    class Meta:
        fields =(
            'id',
            'username',
            'password',
            'email',
            'is_admin',
            'is_active',
            'is_staff',
            'is_superuser',
            
        )
        model = User
    



      
   