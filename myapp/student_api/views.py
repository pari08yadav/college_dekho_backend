from django.shortcuts import render, redirect
from myapp.models import Student
from .serializers import StudentSerializer 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from myapp.pagination import CustomPagination
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail


# creating a signup api for Student using api_view 
@api_view(['POST'])
@csrf_exempt
def student_signup(request):
    # if request.user.is_authenticated:
    user_email = request.data.get('email')     #fetching user email.
    request.data._mutable = True   #with thid code queryset converted into mutable form
    data = request.data    #storing all sended data in data variable
    hashed_password = make_password(data.get('password'))  # hashing password
    data['password'] = hashed_password         #updating old password with hashed password
    
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
        if serializer.save():
            # Compose email message
          subject = 'Welcome to Our Platform!'
          body = 'Thank you for signing up. We are excited to have you on board!'
          sender_email = 'yadav.parishram@gmail.com'  # Replace with your sender email address
          recipient_email = user_email

          # Send email
          send_mail(subject, body, sender_email, [recipient_email], fail_silently=False,)
          
        return Response({"message":"Your signup is done successfull", "serializer data":serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # else:
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)
    


# Creating login api for Student using api_view decorator
@api_view(['POST'])
@csrf_exempt
def student_login(request):
    # if request.user.is_authenticated:
        if not request.user.is_authenticated:
            username = request.data.get('username')
            password = request.data.get('password')
            print(username)
            print(password)
            user = Student.objects.get(username=username, password=password)
            if user:
                return Response({'message': 'Login successful', 'user': StudentSerializer(user).data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response("You are already Logged In.")
    
    # else:
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)
