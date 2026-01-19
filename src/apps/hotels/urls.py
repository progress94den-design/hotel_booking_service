from django.urls import path

from apps.hotels.views import HotelViewSet

urlpatterns = [
    path(
        "", HotelViewSet.as_view({"get": "list", "post": "create"}), name="hotels_list"
    ),
    path(
        "<int:hotel_id>/",
        HotelViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="hotels_detail",
    ),
]
