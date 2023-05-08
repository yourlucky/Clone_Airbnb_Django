from django.urls import path
from . import views

urlpatterns = [
    path("amenities/",views.Amenities.as_view()),
    path("amenities/<int:pk>",views.AmenityDetail.as_view()),
    path("",views.Rooms.as_view()),
    path("<int:pk>",views.RoomDetail.as_view()),
    path("<int:pk>/reviews",views.RoomReviews.as_view()),
    path("<int:pk>/amenities",views.RoomAmenities.as_view()),

]

# urlpatterns =[
#     path("",views.see_all_rooms),
#     path("<int:room_pk>",views.see_one_room),

# ]