from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from user_app.api.views import registration_view, logout_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("login/", obtain_auth_token, name="login"),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("register/", registration_view, name="register"),
    path("logout/", logout_view, name="logout"),

    # path("watch/", include('watchlist_app.api.urls')),
    # path("account/", include('user_app.api.urls')),
    # path('api-auth', include('rest_framework.urls')),
]


