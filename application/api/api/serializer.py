from rest_framework import serializers

from .models.users import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ("username", "birth_date", "created", "updated")
        fields = "__all__"
