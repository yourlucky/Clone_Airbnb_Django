from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from rooms.models import Room
from .models import Wishlist

from django.shortcuts import render
from .serializers import WishlistSerializer

# Create your views here.

class Wishlists(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_wishlists = Wishlist.objects.filter(user=request.user)
        serializer = WishlistSerializer(all_wishlists, many=True, context={"request":request},)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            wishlist=serializer.save(
                User=request.user,
            )
            serializer = WishlistSerializer(wishlist)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
class WishlistDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk,user):
        try:
            return Wishlist.objects.get(pk=pk, user=user)
        except Wishlist.DoesNotExist:
            return NotFound
        

    def get(self, request, pk):
        Wishlist = self.get_object(pk, request.user)
        serializer = WishlistSerializer(Wishlist, context={"request": request})
        return Response(data=serializer.data)
    
    def delete(self, request, pk):
        wishlist = self.get_object(pk, request.user)
        wishlist.delete()
        return Response(status=HTTP_200_OK)
    
    def put(self,request,pk):
        wishlist = self.get_object(pk, request.user)
        serializer = WishlistSerializer(wishlist, data=request.data, partial=True,)
        if serializer.is_valid():
            serializer.save()
            serializer = WishlistSerializer(wishlist)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def get_authenticate_header(self, request):
        return super().get_authenticate_header(request)
    
class WishlistToggle(APIView):
    def get_list(self, pk, user):
        try:
            return Wishlist.objects.get(pk=pk, user=user)
        except Wishlist.DoesNotExist:
            raise NotFound

    def get_room(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def put(self, request, pk, room_pk):
        wishlist = self.get_list(pk, request.user)
        room = self.get_room(room_pk)
        if wishlist.rooms.filter(pk=room.pk).exists():
            wishlist.rooms.remove(room)
        else:
            wishlist.rooms.add(room)
        return Response(status=HTTP_200_OK)


        