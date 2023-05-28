from django.db import models

# Create your models here.

# build fields from : Loan_ID	Gender	Married	Dependents	Education	Self_Employed	ApplicantIncome	CoapplicantIncome	LoanAmount	Loan_Amount_Term	Credit_History	Property_Area	Loan_Status 

class Loan(models.Model):
    
    Genders = (
        ('male', 'Male'),
        ('female','Female'),
        ('nan', 'Nan')
        
    )
    
    Married = (
        ('yes', 'Yes'),
        ('no', 'No'),
        ('nan', 'Nan')
    )
    
    Education=(
        ('graduate', 'Graduate'),
        ('notgraduate', 'Not Graduate')
    )
    
    Dependents=(
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3+', '3+'),
        ('nan', 'Nan')
    )
    
    Self_Employed=(
        ('yes', 'Yes'),
        ('no', 'No'),
        ('nan', 'Nan')
    )
    
    Property_Area=(
        ('rural', 'Rural'),
        ('semiurban', 'Semiurban'),
        ('urban', 'Urban')
    )
    
    loan_id = models.IntegerField(primary_key=True, unique=True, null=False)
    
    gender = models.CharField(choices=Genders, max_length=6)
    
    married = models.CharField(choices=Married, max_length=3)
    
    dependents = models.CharField(choices=Dependents, max_length=5)
    
    education = models.CharField(choices=Education, max_length=12)
    
    self_employed = models.CharField(choices=Self_Employed, max_length=3)
    
    property_area = models.CharField(choices=Property_Area, max_length=9)
    
    applicant_income = models.IntegerField()
    
    coapplicant_income = models.FloatField()
    
    loan_amount = models.FloatField()
    
    loan_amount_term = models.FloatField()
    
    credit_history = models.FloatField()
    
    loan_status = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.loan_id)