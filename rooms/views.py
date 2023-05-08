from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction

from .models import Amenity, Room
from .serializers import AmenitySerializer, RoomListSerializer, RoomDetailSerializer

from categories.models import Category

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, NotAuthenticated, ParseError, PermissionDenied
from rest_framework.status import HTTP_204_NO_CONTENT

from reviews.serializers import ReviewSerializer

class Amenities(APIView):
    
    def get(self,request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(all_amenities,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            amenity = serializer.save()
            return Response(AmenitySerializer(amenity).data,)

        else:
            return Response(serializer.errors)


class AmenityDetail(APIView):

    def get_object(self,pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            return NotFound

    def get(self,request,pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity)
        return Response(serializer.data)

    def put(self,request,pk):
        amentiy=self.get_object(pk)
        serializer = AmenitySerializer(amentiy,data=request.data,partial=True,)
        if serializer.is_valid():
            updated_amenity = serializer.save()
            return Response(AmenitySerializer(updated_amenity).data,)
        else:
            return Response(serializer.errors)

    def delete(self,request,pk):
        amenity=self.get_object(pk)
        amenity.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Rooms(APIView):

    def get(self,request):
        all_rooms = Room.objects.all()
        serializer = RoomListSerializer(all_rooms,many=True, context={"request":request})
        
        return Response(serializer.data)
    
    def post(self,request):
        if request.user.is_authenticated:
            serializer = RoomDetailSerializer(data=request.data)
            if serializer.is_valid():
                category_pk = request.data.get("category")
                if not category_pk:
                    raise ParseError("Category is required")
                try :
                    category = Category.objects.get(pk=category_pk)
                    if category.kind == Category.CategoryKindChoices.EXPERIENCES:
                        raise ParseError("The category kind should be 'rooms'")
                except Category.DoesNotExist:
                        raise ParseError("Category does not exist")
                try:
                    with transaction.atomic(): 
                        room = serializer.save(owner=request.user, category=category)
                        amenties = request.data.get("amenities")
                        for amenity_pk in amenties:
                            amenity = Amenity.objects.get(pk=amenity_pk)
                            room.amenities.add(amenity)
                        serializer=RoomDetailSerializer(room)
                        return Response(serializer.data,)
                except Exception :
                    raise ParseError("Amenitiy error")
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated
        
class RoomDetail(APIView):
    def get_object(self,pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request,pk):
        room = self.get_object(pk)
        serializer = RoomDetailSerializer(room, context={"request":request},)
        return Response(serializer.data)
    
    def put(self, request, pk):
        room = self.get_object(pk)

        if not request.user.is_authenticated:
            raise NotAuthenticated

        if room.owner != request.user:
            raise PermissionDenied

        serializer = RoomDetailSerializer(
            room,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            category_pk = request.data.get("category")
            if category_pk:
                try:
                    category = Category.objects.get(pk=category_pk)
                    if category.kind == Category.CategoryKindChoices.EXPERIENCES:
                        raise ParseError("The category kind should be rooms")
                except Category.DoesNotExist:
                    raise ParseError(detail="Category not found")

            try:
                with transaction.atomic():
                    if category_pk:
                        room = serializer.save(category=category)
                    else:
                        room = serializer.save()

                    amenities = request.data.get("amenities")
                    if amenities:
                        room.amenities.clear()
                        for amenity_pk in amenities:
                            amenity = Amenity.objects.get(pk=amenity_pk)
                            room.amenities.add(amenity)

                    return Response(RoomDetailSerializer(room).data)
            except Exception as e:
                print(e)
                raise ParseError("amenity not found")
        else:
            return Response(serializer.errors)
    

    
    def delete(self,request,pk):
        room = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if room.owner != request.user:
            raise PermissionDenied
        room.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class RoomReviews(APIView):

    def get_object(self,pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        try:
            page=request.query_params.get("page",1)
            page= int (page)
        except ValueError:
            page=1
        page_size = 3
        start = (page -1) * page_size
        end = start + page_size
        room = self.get_object(pk)
        serializer = ReviewSerializer(room.reviews.all()[start:end],many=True)
        return Response(serializer.data)

class RoomAmenities(APIView):

    def get_object(self,pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self,request,pk):
        try:
            page=request.query_params.get("page",1)
            page= int (page)
        except ValueError:
            page = 1
        page_size = 3
        start = (page-1) * page_size
        end= start + page_size
        
        room = self.get_object(pk)
        serializer = AmenitySerializer(room.amenities.all()[start:end],many=True)
        return Response(serializer.data)

