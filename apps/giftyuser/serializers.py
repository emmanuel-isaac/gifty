from rest_framework import routers, serializers, viewsets
from apps.giftyuser.models import User


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'username', 'email', 'phone', 'address', 'is_staff')

