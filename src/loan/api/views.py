from rest_framework import generics
from .serializers import LoanSerializer, CreateLoanSerializer, UpdateLoanSerializer
from loan.models import Loan

class DisplayLoanAPIView(generics.RetrieveAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    
class CreateLoanAPIView(generics.CreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = CreateLoanSerializer
    
class UpdateLoanAPIView(generics.UpdateAPIView):
    queryset = Loan.objects.all()
    serializer_class = UpdateLoanSerializer
    
class DeleteLoanAPIView(generics.DestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
