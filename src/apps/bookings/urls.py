from django.urls import path
from apps.bookings.views import BookingViewSet

urlpatterns = [
    path(
        "",
        BookingViewSet.as_view({"get": "list", "post": "create"}),
        name="bookings_list",
    ),
    path(
        "<int:hotel_id>/",
        BookingViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="bookings_detail",
    ),
]
