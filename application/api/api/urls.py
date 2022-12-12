from django.urls import path, include
from rest_framework import routers

from .views import UsersViewSet, FilterUsersList

router = routers.DefaultRouter()  # url manager
router.register("users", UsersViewSet, basename="users")  # url registering on url manager

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),  # adding all urls managed by url manager
    path("users/<str:key>/<str:value>/", FilterUsersList.as_view()),
]
