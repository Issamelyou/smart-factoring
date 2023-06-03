from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from .serializers import (
    CustomTokenObtainPairSerializer,
    UserRegisterSerializer,
    AccountChangePasswordSerializer,
    # CustomerSignUpSerializer,
    # MecanicSignUpSerializer,
    # CustomerLoginSerializer,
    # MecanicLoginSerializer,
)

User = get_user_model()

class AccountLoginView(TokenObtainPairView):
    """This Api allow user to login, by providing username and password and creating for them a JWT token"""

    permission_classes = (AllowAny,)
    serializer_class = CustomTokenObtainPairSerializer

class UserRegisterView(generics.CreateAPIView):
    """Register view, which allow user to sign up and create a new account"""

    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer

class AccountChangePasswordView(generics.UpdateAPIView):
    """This api allow you to update user password"""

    permission_classes = (IsAuthenticated,)
    serializer_class = AccountChangePasswordSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response(
            {"detail": "Password updated successfully"}, status=status.HTTP_200_OK
        )

# class SignUpCustomerAPI(generics.GenericAPIView):
#     serializer_class = CustomerSignUpSerializer
#     permission_classes = [permissions.AllowAny]

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         customer = serializer.save()
#         return Response(
#             {
#                 "customer": CustomerSignUpSerializer(
#                     customer, context=self.get_serializer_context()
#                 ).data,
#             }
#         )


# class SignUpMecanicAPI(generics.GenericAPIView):
#     serializer_class = MecanicSignUpSerializer
#     permission_classes = [permissions.AllowAny]

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         mecanic = serializer.save()
#         return Response(
#             {
#                 "mecanic": MecanicSignUpSerializer(
#                     mecanic, context=self.get_serializer_context()
#                 ).data,
#             }
#         )


# class LoginCustomerAPI(generics.GenericAPIView):
#     serializer_class = CustomerLoginSerializer
#     permission_classes = [permissions.AllowAny]

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         account = serializer.validated_data
#         return Response(
#             {
#                 "customer": CustomerLoginSerializer(
#                     account, context=self.get_serializer_context()
#                 ).data,
#             }
#         )


# class LoginMecanicAPI(generics.GenericAPIView):
#     serializer_class = MecanicLoginSerializer
#     permission_classes = [permissions.AllowAny]

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         nursery = serializer.validated_data
#         return Response(
#             {
#                 "mecanic": MecanicLoginSerializer(
#                     nursery, context=self.get_serializer_context()
#                 ).data,
#             }
#         )