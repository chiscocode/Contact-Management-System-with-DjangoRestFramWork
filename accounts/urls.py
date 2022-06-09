from django.urls import path
from . import views
# register, login and logout
from .views import *
from knox import views as knox_views

urlpatterns = [
    path('contact/', views.ContactListAPIView.as_view()),
    path('contact/post/',views.ContactCreateAPIView.as_view()),
    path('contact/update/<int:pk>',views.ContactUpdateAPIView.as_view()),
    path('contact/delete/<int:pk>',views.ContactRetrieveDestroyAPIView.as_view()),
    # pickup
    path('pickup/', views.PickupListAPIView.as_view()),
    path('pickup/post/',views.PickupCreateAPIView.as_view()),
    path('pickup/update/<int:pk>',views.PickupUpdateAPIView.as_view()),
    path('pickup/delete/<int:pk>',views.PickupRetrieveDestroyAPIView.as_view()),

    # autheticatication
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),



]

