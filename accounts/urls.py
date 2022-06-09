from django.urls import path
from . import views
# register, login and logout
from .views import *
from knox import views as knox_views

urlpatterns = [
    path('contact/', views.contactList),
    path('contact/<int:pk>',  views.contactDetail), # to capture our ids
    path('post/',views.contactPost),
    path('update/<int:pk>',views.contactUpdate),
    path('delete/<int:pk>',views.contactDelete),
    # pickup
    path('pickup/', views.pickupList),
    path('pickup/<int:pk>',  views.pickupDetail), # to capture our ids
    path('pickup/post/',views.pickupPost),
    path('pickup/update/<int:pk>',views.pickupUpdate),
    path('pickup/delete/<int:pk>',views.pickupDelete),

    # autheticatication
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    # serch functionality
    path('track/',views.PickupAPIView.as_view(), name='search'),



]

