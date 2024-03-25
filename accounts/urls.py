from django.urls import path
from .views import * 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/', RegisterApi.as_view()),
    path('login/', LoginAPI.as_view()),
    # path('login/', LoginView.as_view()),
    
    path('enquiry/', EnquiryApi.as_view()),
    path('admin/login/', AdminLoginView.as_view(), name='admin-login'),

    path('changepassword/', ChangePasswordApi.as_view()),

    # path('forgotpassword/', ForgotPasswordApi.as_view()),
    path('verificationpassword/', VerificationOtpApi.as_view()),
    # path('setnewpassword/', SetNewPasswordApi.as_view()),
    # path('setnewpassword/', ResetPasswordAPI.as_view()),
    # path('forgotpassword/', ForgotPasswordApi1.as_view()),

    path('forgetpassword/',ForgotPasswordApi.as_view(), name = 'forget-password'),
    path('verifyotp/',VerificationOtpApi.as_view(), name = 'verify-otp' ),
    path('setpwd/',SetNewPasswordApi.as_view(), name = 'set-pwd'),



    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
