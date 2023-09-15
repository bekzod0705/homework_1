from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import todoModel
from .serializer import ToDoSerializer
from rest_framework import generics
import datetime
# Create your views here.

# class getAll(APIView):
#     def get(self,request):
#         some=todoModel.objects.all()
#         serializer=ToDoSerializer(some,many=True)
#         return Response(serializer.data)

class getAllCreate(generics.ListCreateAPIView):
    queryset=todoModel.objects.all()
    serializer_class=ToDoSerializer

# class getDetail(APIView):
#     def get(self,request,*args,**kwargs):
#         x=get_object_or_404(todoModel,id=kwargs['forid'])
#         serializer=ToDoSerializer(x)
#         return Response(serializer.data)

class DetailDestroyUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=todoModel.objects.all()
    serializer_class=ToDoSerializer
    
# class create(APIView):
#     def post(self,request):
#         serializer=ToDoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.error)
    

# class change(APIView):
#     def patch(self,request,*args,**kwargs):
#         x=get_object_or_404(todoModel,id=kwargs['forid'])
#         serializer=ToDoSerializer(x,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.error)
    


class put(APIView):
    def patch(self,request,*args,**kwargs):
        x=get_object_or_404(todoModel,id=kwargs['forid'])
        serializer=ToDoSerializer(x,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)

# class delete(APIView):
#     def delete(self,request,*args,**kwargs):
#         x=get_object_or_404(todoModel,id=kwargs['forid'])
#         x.delete()
        






class today(APIView):
    def get(self,request,*args,**kwargs):
        today=datetime.date.today()
        x=todoModel.objects.filter(created_at__date=today)
        serializer=ToDoSerializer(x,many=True)
        return Response(serializer.data)

class lastTen(APIView):
    def get(self,request,*args,**kwargs):
        today=datetime.datetime.now()
        last_ten=today-datetime.timedelta(days=10)
        x=todoModel.objects.filter(created_at__gte=last_ten,created_at__lte=today)
        serializer=ToDoSerializer(x,many=True)
        return Response(serializer.data)

class status(APIView):
    def get(self,request,*args,**kwargs):
        today=datetime.date.today()
        x=todoModel.objects.filter(created_at__date=today,status=True)
        serializer=ToDoSerializer(x,many=True)
        return Response(serializer.data)
