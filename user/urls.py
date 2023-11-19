from django.contrib import admin
from django.urls import path
from user import views
from user.views import RegisterAPIView, ConfirmAPIView, LoginAPIView

# urlpatterns = [
#     path('users/registration/', views.register_api_view),
#     path('users/confirm/', views.confirm_api_view),
#     path('users/authorization/', views.login_api_view),
# ]

urlpatterns = [
    path('user/registration/', RegisterAPIView.as_view()),
    path('user/confirm/', ConfirmAPIView.as_view()),
    path('user/login/', LoginAPIView.as_view()),
]