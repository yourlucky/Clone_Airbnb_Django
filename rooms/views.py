from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
from .models import Amenity
from .serializers import AmenitySerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT

class Amenities(APIView):
    
    def get(self,request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(all_amenities,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            amenity = serializer.save()
            return Response(AmenitySerializer(amenity).data)

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




# def see_all_rooms(request):
#     rooms = Room.objects.all()
#     return render(request, "all_rooms.html",
#                   {
#                     'rooms':rooms,
#                     'title':"hello! this title comes from django!",
#                     },
#             )
# # Create your views here.
# def see_one_room(request,room_pk):
#     try :
#         rooms = Room.objects.get(pk=room_pk)
#         return render(request, "all_rooms.html",
#                       {
#                         'rooms':rooms,
#                         'title':"hello! this title comes from django!",
#                         },
#                 )
#     except Room.DoesNotExist:
#         return render(request,"room_detail.html",{'Not_found':True,},)


