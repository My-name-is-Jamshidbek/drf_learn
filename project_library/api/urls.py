from django.urls import path

from .views import BookAPIView


urlpatterns = [
    path("", BookAPIView.as_view(), name="api_v1_book_list")
]

