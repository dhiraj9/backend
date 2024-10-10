from django.shortcuts import render
from .models import CustomUser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer,LoginSerializer
from django.contrib.auth import authenticate

#this is for after accessing jwt token in postman
class HomeView(APIView):
   permission_classes = [IsAuthenticated]
   
   def get(self,request):
      return Response({"Product Home:The app is up and running."})


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class =RegisterSerializer

class LoginView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = LoginSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception =True)
        user =authenticate(email =serializer.validated_data['email'],
                           password =serializer.validated_data['password'])
            
        if user:
         refresh =RefreshToken.for_user(user)
         return Response({'refresh':str(refresh),
                       'access':str(refresh.access_token),},
                       status= status.HTTP_200_OK)
        return Response({
           'error': 'Invalid Credentials'
                        },
                        status=status.HTTP_401_UNAUTHORIZED)
    
    