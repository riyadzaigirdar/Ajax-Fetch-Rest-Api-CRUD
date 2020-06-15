from django.shortcuts import render
from .models import Task
from .serialzers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

@api_view(['GET'])
def api_root(request):
    api_urls = {
        'task-list': '/list/',
        'task-create': '/create/',
        'task-detail': '/detail/<int:pk>/',
        'task-update':'/detail/<int:pk>/',
        'task-delete':'/delete/<int:pk>/',
    }
    return Response(api_urls)

'''
@api_view(['GET','POST'])
def tasklist(request):
    
    if request.GET.get('title'):
        title = request.GET['title']
        task = Task.objects.filter(title = title)
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)	
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    task = Task.objects.all()
    serializer = TaskSerializer(task, many = True)
    return Response(serializer.data)
'''
class tasklist(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = Task.objects.all().order_by('-id')
        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(title=title)
        return queryset

@api_view(['GET'])
def taskdetail(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(task)
    return Response(serializer.data)

@api_view(['DELETE'])
def taskdelete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return Response(' Task Deleted')

@api_view(['GET','PUT','POST'])
def taskupdate(request,pk):
    task = Task.objects.get(pk=pk)

    if request.method == 'GET':
    	serializer = TaskSerializer(task)
    	return Response(serializer.data)
    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
    	serializer.save()
    return Response(serializer.data)

@api_view(['GET','POST'])
def taskcreate(request):
    serializer = TaskSerializer(data=request.data)
    print("I am out")
    if serializer.is_valid():
        print('i am in')
        serializer.save()
    return Response(serializer.data)


