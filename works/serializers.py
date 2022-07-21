from rest_framework import serializers
from .models import Shift


class ShiftSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        fields = '__all__'
        extra_fields = ['user_id']
        extra_kwargs = {
            'user': {'read_only': True}
        }
        model = Shift
