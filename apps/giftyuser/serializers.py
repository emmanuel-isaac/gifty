from rest_framework import routers, serializers, viewsets
from apps.giftyuser.models import User, StaffMember


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'username', 'email', 'phone', 'address', 'is_staff')


class StaffMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StaffMember
        fields = ('url', 'user')

