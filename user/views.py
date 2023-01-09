from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from .serializers import RegisterSerializer
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

# Create your views here.

class RegisterView(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    # overwriting the parent class' method to create a new token when user register
    def create(self, request, *args, **kwargs):

        response = super().create(request, *args, **kwargs)

        token = Token.objects.create(user_id = response.data["id"])
        response.data["token"] = token.key

        return response
