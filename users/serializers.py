from attr import fields
from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Account
        extra_kwargs = {
            'password': {'write_only': True}
        }
