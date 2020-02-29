# from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import userProfile
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import userProfileSerializer


# Create your views here.

class UserProfileListCreateView(ListCreateAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer =save(user=user)


# class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
#     queryset=userProfile.objects.all()
#     serializer_class=userProfileSerializer
#     permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]
class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]
