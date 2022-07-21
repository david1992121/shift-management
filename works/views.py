from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated
from .models import Shift
from .serializers import ShiftSerializer


class IsOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH", "DELETE"]:
            return obj.user == request.user
        return True


class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    ordering = ('-date')
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    def get_queryset(self):
        user = self.request.user
        return Shift.objects.filter(user=user).order_by('-date')
