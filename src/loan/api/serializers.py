from loan.models import Loan
from rest_framework import serializers
from ..utils import predict_loan_status

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        exclude = ('loan_id',)
        
class CreateLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        exclude = ('loan_id', 'loan_status')
        
    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        # predict the loan status
        data = list(validated_data.values())
        prediction = predict_loan_status(data)
        validated_data['loan_status'] = bool(prediction[0])
        return super().create(validated_data)
        
        
    
    
class UpdateLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        exclude = ('loan_id', 'loan_status')
        
    def validate(self, attrs):
        return super().validate(attrs)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    