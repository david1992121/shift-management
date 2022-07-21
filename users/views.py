from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from users.serializers import AccountSerializer
from .models import Account
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class AccountView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            input_data = serializer.validated_data
            username = input_data.get('username')
            password = input_data.get('password')

            # create user and set password
            user = Account.objects.create(username=username)
            user.set_password(password)
            user.save()
            return Response(AccountSerializer(user).data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
