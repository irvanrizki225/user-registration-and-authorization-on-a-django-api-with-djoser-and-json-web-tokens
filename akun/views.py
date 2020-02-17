# from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import userProfile
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import userProfileSerializer

# Create your views here.

class UserProfileListCreateView(ListCreateAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    permission_class=[IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer =save(user=user)


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=userProfile.objects.all()
    serializer_class = userProfileSerializer
    permission_class = [IsOwnerProfileOrReadOnly,IsAuthenticated]
