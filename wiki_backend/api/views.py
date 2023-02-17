

# Create your views here.
from . import serializers
from django.conf import settings

import random


from django.contrib.auth import login
from django.contrib.auth import logout
from django.core.mail import send_mail
# from django.contrib.auth import authenticate

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.views import APIView

class LoginView(APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        # if authenticate(request) !=None:
        #     return 
        serializer = serializers.LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)


class Authentication(APIView):
    """
    check if the client is authenticated or not, if authenticated, return the client information
    """
    
    permission_classes=(permissions.AllowAny,)

    def get(self,request):
        user = request.user
        # if user is logged in
        if user.is_authenticated:
            serializer = serializers.UserSerializer(user)
            return Response(serializer.data)
        # else 
        else:
            return Response({'unauthenticated':True})


class LogoutView(APIView):

    permission_classes=(permissions.IsAuthenticated,)

    def get(self,request):
        logout(request)
        return Response(None,status= status.HTTP_202_ACCEPTED)


class SignUpView(APIView):

    permission_classes=(permissions.AllowAny,)

    def post(self, request): 
        serializer = serializers.SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')
        login(request,user)
        return Response({'msg':"Account has been successfully signed up !"})



class SendEmailView(APIView):

    permission_classes=(permissions.AllowAny,)

    def post(self,request):
        serializer = serializers.SendEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg':"Email has sent!",'code': 200})

class CheckDuplication(APIView):
    
    def post(self,request):
        serializer = serializers.CheckDuplicationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg':"The username is okay",'code':200})
    
class CreateEntry(APIView):
    """
    Crete or update the current entry
    """

    permission_classes=(permissions.IsAuthenticated,)
    
    def get(self,request):
        serializer = serializers
        

