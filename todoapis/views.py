from rest_framework.views import APIView
from rest_framework import serializers,status
from rest_framework.response import Response

from .serializers import TodoSerializer
from . models import Todo

# Create your views here.


class TodoGetView(APIView):
    def get(self,request):
        try:
            todo = Todo.objects.all()
            serializer = TodoSerializer(todo, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error',str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # post
    def post(self,request):
        try:
            serializer = TodoSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'Message':'Error in data'},status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error',str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

class TodoDetailView(APIView):
    # get a single item
    def get(self,request,*args,**kwargs):
        todo_id = kwargs.get('id')
        try:
            todo = Todo.objects.get(id=todo_id)
            serializer = TodoSerializer(todo)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error',str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # update
    def put(self,request,*args,**kwargs):
        todo_id = kwargs.get('id')
        try:
            todo = Todo.objects.get(id=todo_id)
            serializer = TodoSerializer(instance=todo, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response({'Message': 'Invalid Todo id'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error',str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # delete
    def delete(self, request,id):
        try:
            todo = Todo.objects.get(id=id)
            todo.delete()
            return Response({'success':'Item deleted'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error',str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)