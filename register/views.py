from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import *
from .permissions import IsOwner
from .models import Register

class RegisterView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RegisterSerializer

    def get_queryset(self):
        year = self.request.GET.get("year")
        month = self.request.GET.get("month")
        day = self.request.GET.get("day")

        if year and month and day:
            queryset = Register.objects.order_by("date").filter(user_id=self.request.user.id, date__icontains=f"{year}-{month}-{day}")
            return queryset
        
        if year and month:
            queryset = Register.objects.order_by("date").filter(user_id=self.request.user.id, date__icontains=f"{year}-{month}")
            return queryset
        
        if year:
            queryset = Register.objects.order_by("date").filter(user_id=self.request.user.id, date__icontains=f"{year}")
            return queryset
        
        return Register.objects.order_by("date").filter(user_id=self.request.user.id)
    
    def create(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.validated_data, status=201)

    def perform_create (self, serializer):
        serializer.save(user=self.request.user)


class RegisterDetailsView(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = "id" 
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = RegisterSerializerDetails

    def get_queryset(self):
        return Register.objects.filter(id=self.kwargs['id'])

class RegisterResume(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RegisterResumeSerializer

    def get(self, request, *args, **kwargs):
        year = self.request.GET.get("year")
        month = self.request.GET.get("month")
        day = self.request.GET.get("day")

        queryset = Register.objects.filter(user_id=self.request.user.id)

        if year and month and day:
            queryset = Register.objects.filter(user_id=self.request.user.id, date__icontains=f"{year}-{month}-{day}")
        
        if year and month:
            queryset = Register.objects.filter(user_id=self.request.user.id, date__icontains=f"{year}-{month}")
        
        if year:
            queryset = Register.objects.filter(user_id=self.request.user.id, date__icontains=f"{year}")
        
        registers = queryset
        serializer_registers = RegisterResumeSerializer(registers)

        return Response(serializer_registers.data)