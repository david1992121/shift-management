from attr import fields
from rest_framework import serializers

from works.serializers import ShiftSerializer
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    shifts = ShiftSerializer(read_only=True, many=True)

    class Meta:
        fields = '__all__'
        extra_fields = ['shifts']
        model = Account
        extra_kwargs = {
            'password': {'write_only': True}
        }
