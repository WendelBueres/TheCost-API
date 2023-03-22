from rest_framework import serializers
from .models import User
import ipdb

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = [
            "first_name",
            "last_name",
            "email",
            "password"
        ]

        extra_kwargs = {"password": {"write_only": True}}


    def create(self, validated_data: dict):
        validated_data["username"] = validated_data["email"]
        user = User.objects.create_user(**validated_data)

        return user
    