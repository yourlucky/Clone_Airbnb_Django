from rest_framework.serializers import ModelSerializer
from .models import User


class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "avatar",
        )

class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model=User
        exclude = (
            "password",
            "is_superuser",
            "id",
            "is_staff",
            "is_host",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        )