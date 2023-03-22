from rest_framework import permissions
from .models import Register
from django.shortcuts import *

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        register = get_object_or_404(Register, id=request.parser_context['kwargs']['id'])
        
        return request.user.id == register.user_id