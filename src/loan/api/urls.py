from django.urls import path
from .views import *

urlpatterns = [
    path('display/<int:pk>/', DisplayLoanAPIView.as_view()),
    path('create/', CreateLoanAPIView.as_view()),
    path('update/<int:pk>/', UpdateLoanAPIView.as_view()),
    path('delete/<int:pk>/', DeleteLoanAPIView.as_view()),
]

    
    
