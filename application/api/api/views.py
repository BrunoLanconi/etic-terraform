from datetime import datetime

from django.core.exceptions import ValidationError, FieldError
from django.http import Http404
from rest_framework import viewsets, generics

# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

from .models.users import User
from .serializer import UsersSerializer


class UsersViewSet(viewsets.ModelViewSet):  # all-in-one request method treatment (GET, POST, PUT, UPDATE)
    """
    Shows all users
    """
    queryset = User.objects.all()  # what will be returned
    serializer_class = UsersSerializer  # who will serialize returned content
    # authentication_classes = [BasicAuthentication]  # authentication method
    # permission_classes = [IsAuthenticated]  # authentication verification method


class FilterUsersList(generics.ListAPIView):
    """
    Shows all users based on key and value
    """
    def get_queryset(self):
        try:
            if self.kwargs["key"] in ["username"]:
                query = {self.kwargs["key"] + "__icontains": self.kwargs["value"]}
                queryset = User.objects.filter(**query)

            elif self.kwargs["key"] in ["birth_date", "created", "updated"]:
                datetime_timestamp = datetime.timestamp(self.kwargs["value"])
                query = {self.kwargs["key"] + "__date_gte": datetime_timestamp}
                queryset = User.objects.filter(**query)

            else:
                queryset = User.objects.filter(**{self.kwargs["key"]: self.kwargs["value"]})

        except (ValidationError, FieldError, TypeError):
            raise Http404
        return queryset

    serializer_class = UsersSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
