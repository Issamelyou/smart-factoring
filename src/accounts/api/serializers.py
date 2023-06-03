from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from django.core.mail import send_mail
from django.contrib.auth import authenticate

User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(CustomTokenObtainPairSerializer, cls).get_token(user)
        # Add custom claims
        token['email'] = user.email
        return token

    def validate(self, attrs):
        # override to also display user info
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data['user'] = AccountProfileSerializer(self.user).data
        return data


class AccountProfileSerializer(serializers.ModelSerializer):
    """Account profile serializer"""

    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'first_name',
            'last_name',
            'personal_phone',
            'is_customer',
            'is_mecanic',
        )

class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'password2',
            'first_name',
            'last_name',
            'personal_phone',
            'is_customer',
            'is_mecanic',
        )
        extra_kwargs = {
            'personal_phone': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            personal_phone=validated_data['personal_phone'],
            is_customer=validated_data['is_customer'],
            is_mecanic=validated_data['is_mecanic'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class AccountChangePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    new_password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'new_password', 'new_password2')

    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"}
            )
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['new_password'])
        instance.save()
        # send email notification that password has been changed
        return instance



# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email', 'username', 'password']
#         extra_kwargs = {'password': {'write_only': True}}


# class CustomerSignUpSerializer(serializers.ModelSerializer):
#     user = UserSerializer(many=False)

#     class Meta:
#         model = Customer
#         fields = ['user', 'first_name', 'last_name']

#     def create(self, validated_data):
#         user_data = validated_data.pop('user')
#         customer = Customer.objects.create(**validated_data)
#         User.objects.create(customer=customer, **user_data)
#         return customer

#     def save(self, validated_data, **kwargs):
#         user = User.objects.create_user(
#             email=validated_data['email'],
#             username=validated_data['username'],
#             password=validated_data['password'],
#         )
#         user.save()
#         return user


# class MecanicSignUpSerializer(serializers.ModelSerializer):
#     user = UserSerializer(many=False)

#     class Meta:
#         model = Mecanic
#         fields = ['user', 'first_name', 'last_name']

#     def create(self, validated_data):
#         user_data = validated_data.pop('user')
#         mecanic = Mecanic.objects.create(**validated_data)
#         User.objects.create(mecanic=mecanic, **user_data)
#         return mecanic


# class CustomerLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField()

#     def validate(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError("Incorrect Credentials")


# class MecanicLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField()

#     def validate(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError("Incorrect Credentials")