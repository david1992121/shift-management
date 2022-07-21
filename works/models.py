from secrets import choice
from django.db import models
from users.models import Account

SHIFT_CHOICES = (
    (0, '0-8'),
    (1, '8-16'),
    (2, '16-24'),
)

class Shift(models.Model):
    hour = models.IntegerField(choices=SHIFT_CHOICES, default=0)
    date = models.DateField()
    user = models.ForeignKey(Account, related_name='shifts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)