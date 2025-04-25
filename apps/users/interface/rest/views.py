from rest_framework import viewsets
from apps.users.infraestructure.models import User
from apps.users.interface.rest.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
