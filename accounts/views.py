from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import filters


@api_view(['GET'])
def contactList(request):
    contacts=Contact.objects.all()
    serializer=ContactSerializer(contacts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def contactDetail(request,pk):
    contacts=Contact.objects.get(id=pk)
    serializer=ContactSerializer(contacts, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def contactPost(request):
    serializer=ContactSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def contactUpdate(request,pk):
    contacts=Contact.objects.get(id=pk)
    serializer=ContactSerializer(instance=contacts,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def contactDelete(request,pk):
    contacts=Contact.objects.get(id=pk)
    contacts.delete()
    return Response('Deleted')


