from django.shortcuts import render, redirect
from myapp.models import Student
from .serializers import StudentSerializer 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from myapp.pagination import CustomPagination



# creating a signup api for Student using api_view 
@api_view(['POST'])
@csrf_exempt
def Student_signup(request):
    # if request.user.is_authenticated:
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
