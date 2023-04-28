from rest_framework import serializers
from .models import Category

from rest_framework.serializers import ModelSerializer




class CategorySerializer(serializers.ModelSerializer) :

    class Meta:
        model = Category
        fields = ('id','name')

        #fields = '__all__'
        #exclude = ('name','description')

