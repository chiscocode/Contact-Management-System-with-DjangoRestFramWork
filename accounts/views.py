from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


# from rest_framework import filters

# autheticatication
# register
from rest_framework import generics, permissions
from knox.models import AuthToken

# login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login




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


# pacel

@api_view(['GET'])
def pickupList(request):
    pickups=Pickup.objects.all()
    serializer=PickupSerializer(pickups, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def pickupDetail(request,pk):
    pickups=Pickup.objects.get(id=pk)
    serializer=PickupSerializer(pickups, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def pickupPost(request):
    serializer=PickupSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def pickupUpdate(request,pk):
    pickups=Pickup.objects.get(id=pk)
    serializer=PickupSerializer(instance=pickups,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def pickupDelete(request,pk):
    pickups=Pickup.objects.get(id=pk)
    pickups.delete()
    return Response('Deleted')

class PickupAPIView(generics.GenericAPIView):
    queryset = Pickup.objects.all()
    serializer_class = PickupSerializer
    # filter_backends = [filters.SearchFilter]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['uuid', 'sendername']
    search_fields = ['=uuid', 'sendername']
    ordering_fields = ['sendername', 'uuid']
    ordering = ['uuid']


# authetication
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


# login
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)