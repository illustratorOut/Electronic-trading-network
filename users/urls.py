from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserListAPIView, UserDetailAPIView, UserUpdateAPIView, UserDeleteAPIView, UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    # User
    path('API/', UserListAPIView.as_view()),
    path('API/<int:pk>/', UserDetailAPIView.as_view()),
    path('API/create/', UserCreateAPIView.as_view()),
    path('API/update/<int:pk>/', UserUpdateAPIView.as_view()),
    path('API/delete/<int:pk>/', UserDeleteAPIView.as_view()),

    # Token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
