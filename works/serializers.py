from attr import validate
from rest_framework import serializers
from .models import Shift, SHIFT_CHOICES


class ShiftSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    hour = serializers.ChoiceField(choices=SHIFT_CHOICES)

    class Meta:
        fields = '__all__'
        extra_fields = ['user_id']
        extra_kwargs = {
            'user': {'read_only': True}
        }
        model = Shift

    def create(self, validated_data):
        if not self.check_date(0, validated_data.get('user_id'), validated_data.get('date')):
            raise serializers.ValidationError(
                {'date': 'The shift already exists'})
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'date' in validated_data.keys():
            if not self.check_date(instance.id, instance.user_id, validated_data.get('date')):
                raise serializers.ValidationError(
                    {'date': 'The shift already exists'})
        return super().update(instance, validated_data)

    def check_date(self, id, user_id, date):
        queryset = Shift.objects.filter(user_id=user_id)
        if int(id) > 0:
            queryset = queryset.exclude(pk=id)
        return queryset.filter(date=date).count() == 0
