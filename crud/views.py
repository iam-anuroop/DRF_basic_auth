from django.shortcuts import render
from .serializer import Studentserilaiser
from .models import Student
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from rest_framework.authentication import BasicAuthentication



class Student_view(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserilaiser
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    

    

    
    


        


        




# Create your views here.
