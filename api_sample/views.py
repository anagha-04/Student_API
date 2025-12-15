
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_sample import serializers
from api_sample.models import StudentModel
from django.shortcuts import get_object_or_404
from api_sample.serializers import studentserializer

# # Create your views here.

# #stud data >> list def get
# #stud data >> add def post
# #stud data >> update def put
# # stud data >> delete def delete 

class StudentListCreateView(APIView):

    def get(self,request):    #used to list all the data from db to the client as response
        student_details = StudentModel.objects.all()   # get all the objects from the model
        serializer = studentserializer(student_details, many =True) #convert into Json
        return Response(serializer.data)
    
    def post(self,request):

        serializer = studentserializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(status= status.HTTP_200_OK)
        
        return Response(status= status.HTTP_400_BAD_REQUEST)
    

class StudentUpdateretrivedeleteView(APIView):

    def get(self,request,**kwargs):

        id = kwargs.get('pk')

        student = get_object_or_404(StudentModel,id=id)

        serializer = studentserializer(student)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,**kwargs):

        id = kwargs.get("pk")

        student = get_object_or_404(StudentModel,id=id)

        serializer = studentserializer(student,data= request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,**kwargs):

      id = kwargs.get("pk")

      student =     get_object_or_404(StudentModel,id=id)

      student.delete()

      return Response({"message":"object deleted successfully"},status=status.HTTP_200_OK)
