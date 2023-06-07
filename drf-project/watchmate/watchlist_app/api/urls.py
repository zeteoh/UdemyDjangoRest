from django.urls import include, path
from watchlist_app.api.views import (WatchListAV, WatchDetailAV, 
                                    StreamPlatformListAV, StreamPlatformDetailAV, 
                                    ReviewListAV, ReviewDetailAV,ReviewCreateAV,
                                    StreamPlatformAV, UserReview, WatchListGV)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'stream', StreamPlatformAV, basename="streamplatform")

"""
    Note: always add an ending `/` to avoid error when running the URL:127.0.0.1:8000/watch/2/
"""
urlpatterns = [
    path("list/", WatchListAV.as_view(), name="movie-list"),
    path("<int:pk>/", WatchDetailAV.as_view(), name="movie-detail"),
    path("list2/", WatchListGV.as_view(), name="watch-list"),

    path('', include(router.urls)),
    # path("stream/", StreamPlatformListAV.as_view(), name="stream-platform"),
    # path("stream/<int:pk>", StreamPlatformDetailAV.as_view(), name="stream-detail"),
    # path('review/', ReviewListAV.as_view(), name="review-list"),
    # path('review/<int:pk>', ReviewDetailAV.as_view(), name="review-detail"),
    path('<int:pk>/review-create/', ReviewCreateAV.as_view(), name="review-create"),

    path('<int:pk>/review/', ReviewListAV.as_view(), name="review-list"),
    path('review/<int:pk>/', ReviewDetailAV.as_view(), name="review-detail"),
    path('review/', UserReview.as_view(), name="user-review-detail"),

]