from django.urls import path, include
from .views import (
    UserRegisterView,
    AccountLoginView,
    AccountChangePasswordView
    # SignUpCustomerAPI,
    # SignUpMecanicAPI,
    # LoginCustomerAPI,
    # LoginMecanicAPI,
)

urlpatterns = [
    path('signup/', UserRegisterView.as_view(), name='register_user'),
    path('login/', AccountLoginView.as_view(), name='login_user'),
    path(
        'change_password/',
        AccountChangePasswordView.as_view(),
        name='my_account_change_password',
    ),
    # path('signup/customer/', SignUpCustomerAPI.as_view(), name='signup_customer'),
    # path('signup/mecanic/', SignUpMecanicAPI.as_view(), name='signup_mecanic'),
    # path('login/customer/', LoginCustomerAPI.as_view(), name='login_customer'),
    # path('login/mecanic/', LoginMecanicAPI.as_view(), name='login_mecanic'),
]