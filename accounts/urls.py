from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contactList),
    path('contact/<int:pk>',  views.contactDetail), # to capture our ids
    path('post/',views.contactPost),
    path('update/<int:pk>',views.contactUpdate),
    path('delete/<int:pk>',views.contactDelete),
   



]

