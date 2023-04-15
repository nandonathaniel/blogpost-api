from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser 
from django.http import JsonResponse
from tryapi.models import Blogpost
from .serializers import BlogpostSerializer, BlogpostSerializer2

@api_view(['POST','GET'])
def controlBlogpost(request):
    if request.method == 'POST':
        serializer = BlogpostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(
            data=serializer.data,
            status=200
        )
    elif request.method == 'GET':
        items = Blogpost.objects.all()
        serializer = BlogpostSerializer2(items, many=True)
        return JsonResponse(
            data=serializer.data,
            safe=False,
            status=200
        )
    
@api_view(['GET', 'PUT', 'DELETE'])
def controlBlogpostId(request, id):
    if request.method == 'GET':
        item = Blogpost.objects.filter(id = id)
        serializer = BlogpostSerializer(item, many=True)
        return JsonResponse(
            data=serializer.data,
            safe=False,
            status=200
        )
    elif request.method == 'PUT':
        item = Blogpost.objects.filter(id = id).first()
        serializer = BlogpostSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                data=serializer.data,
                safe=False,
                status=200
            )
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        Blogpost.objects.filter(id = id).delete()
        return JsonResponse(
            data={
                'message': 'Blogpost deleted successfully'
            },
            status=200
        )