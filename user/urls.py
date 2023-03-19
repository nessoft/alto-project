from django.urls import path
from user.views import UserRegisterViewSet

urlpatterns = [
    path(
        'register', UserRegisterViewSet.as_view(), name='user-register'
    )
]
