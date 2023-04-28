from django.shortcuts import render
#from django.http import JsonResponse
from .models import Category
#from django.core import serializers

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import CategorySerializer
from rest_framework.exceptions import NotFound

from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from rest_framework.viewsets import ModelViewSet


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

# class Categories(APIView):

#     def get(self,request):
#         all_categories = Category.objects.all()
#         serializer = CategorySerializer(all_categories, many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             new_category=serializer.save()
#             return Response(CategorySerializer(new_category).data,)
#         else:
#             return Response(serializer.errors)

# class CategoryDetail(APIView):

#     def get_category(self,pk):
#         try:
#             return Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             raise NotFound(detail="Category not found",code=404)


#     def get(self,request,pk):
#         serializer = CategorySerializer(self.get_category(pk))
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         serializer = CategorySerializer(self.get_category(pk),data=request.data,partial=True)
#         if serializer.is_valid():
#             updated_category=serializer.save()
#             return Response(CategorySerializer(updated_category).data)
#         else:
#             return Response(serializer.errors)
    
    
#     def delete(self,request,pk):
#         self.get_category(pk).delete()
#         return Response(status=HTTP_204_NO_CONTENT)

   


# Create your views here.
