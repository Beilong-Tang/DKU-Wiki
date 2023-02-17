import random

from Entry.models import Client
from .models import Email_Code

from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail

from rest_framework import serializers
# from rest_framework.exceptions import AuthenticationFailed

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(
        label="Username",
        write_only=True,
        max_length = 20,
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True,
        max_length = 26
    )


    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.0
        # It will be used in the view.
        attrs['user'] = user

        return attrs



class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['id','avator']

class UserSerializer(serializers.ModelSerializer):

    client = ClientSerializer(read_only = True)

    class Meta:
        model = User
        fields = ['id','username','client']

class SignUpSerializer(serializers.Serializer):

    username = serializers.CharField(
        max_length = 20,
        min_length = 5,
        label='username'
    )

    email = serializers.EmailField(
        label='email'
    )

    password = serializers.CharField(
        label = 'password',
        style={'input_type': 'password'},
        trim_whitespace = False,
        max_length = 26,
        min_length = 8
    )

    code = serializers.IntegerField(

    )

    def validate(self, data):
        email:str = data.get('email')
        username :str = data.get('username')
        password:str = data.get('password')
        code:int = data.get('code')

        

        if email is None or username is None or password is None or code is None:
            raise serializers.ValidationError('Email, or Username or Password or Code is missing')

        if not email.endswith('@duke.edu'):
            raise serializers.ValidationError('Email has to end up with @duke.edu.')
        
        # Check if there is duplicated user
        if User.objects.filter(username = username).exists():
            raise serializers.ValidationError("The user already exists.")

        if Email_Code.objects.filter(email=email).exists():
            
            email_code = Email_Code.objects.get(email=email)
            
            if email_code.code == code:
                email_code.delete()

            else:
                raise serializers.ValidationError("The verification code is wrong")
            
        else:
            raise serializers.ValidationError("The email does not exist, please input a valide email")


        # create user and client 
        user = User.objects.create_user(username=username,password = password, email =email)
        client = Client.objects.create(user=user)
        
        data['user'] = user

        return data

class SendEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label='email'
    )

    def validate(self, data):
        email = data.get('email')

        if email is None:
            raise serializers.ValidationError("Please send valid email.")
        
        if not email.endswith('@duke.edu'):
            raise serializers.ValidationError("Email has to end up with @duke.edu.")

        code = random.randint(10000,99999)


        if Email_Code.objects.filter(email=email).exists():
            email_code = Email_Code.objects.get(email=email)
            email_code.code = code
            email_code.save()
        
        else:
            email_code = Email_Code.objects.create(email = email, code = code)

        send_mail(subject=settings.SUBJECT, message= settings.MESSAGE % code,   
                  from_email=settings.EMAIL_HOST_USER, recipient_list=[email,])

        return data

class CheckDuplicationSerializer(serializers.Serializer):

    username = serializers.CharField(
        required = False
    )

    email = serializers.CharField(
        required = False
    )

    def validate(self,data):
        username = data.get('username')
        email = data.get('email')
        if username and User.objects.filter(username = username).exists():
            raise serializers.ValidationError(detail={'status':1,'message':"User Duplicate"})

        if email and User.objects.filter(email = email).exists():
            raise serializers.ValidationError(detail={'status':2,'message':"Email Duplicated"})

        return data

