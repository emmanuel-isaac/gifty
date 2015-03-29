from django.shortcuts import render
from apps.giftyuser.serializers import UserSerializer, StaffMemberSerializer
from rest_framework import viewsets
from apps.giftyuser.models import User, StaffMember

# Create your views here.

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StaffMemberViewSet(viewsets.ModelViewSet):
    queryset = StaffMember.objects.all()
    serializer_class = StaffMemberSerializer