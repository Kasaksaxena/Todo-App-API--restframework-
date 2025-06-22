from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import permissions,status
from .models import Todo
from .serializer import TodoSerializer
from django.shortcuts import get_object_or_404
# Create your views here.

#create + get all todos
@api_view(['GET','POST'])
@permission_classes(['permissions.IsAuthenticated'])
def todo_list_create(request):
    if request.method=='GET':
        todos=Todo.objects.filter(user=request.user)
        serializer=TodoSerializer(todos,many=True)
        return Response(serializer.data)
    
    if request.method=="POST":
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#RETRIEVE UPDATE AND DELETE A SPECIFIC TODO
@api_view(['GET','PUT','DELETE'])
@permission_classes([permissions.IsAuthenticated])
def todo_detail(request,uuid):
    todo=get_object_or_404(Todo,uuid=uuid,user=request.user)
    
    if request.method=='GET':
        serializer=TodoSerializer(todo)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=TodoSerializer(todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
    elif request.method=='DELETE':
        todo.delete()
        return Response({'detail':'Deleted'},status=status.HTTP_204_NO_CONTENT)