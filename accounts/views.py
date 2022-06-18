from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# autheticatication
# register
from rest_framework import generics, permissions
from knox.models import AuthToken
# login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login
# permesion
from rest_framework.permissions import AllowAny




# class ContactListAPIView(generics.ListAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer


class ContactCreateAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer




# pacel

class PickupCreateAPIView(generics.CreateAPIView):
    queryset = Pickup.objects.all()
    serializer_class = PickupSerializer
    

class PickupListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Pickup.objects.all()
    serializer_class = PickupSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['uuid', 'sendername']
    search_fields = ['=uuid', 'sendername']
    ordering_fields = ['sendername', 'uuid']
    ordering = ['uuid']


class PickupUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Pickup.objects.all()
    serializer_class = PickupSerializer


class PickupRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Pickup.objects.all()
    serializer_class = PickupSerializer
    






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