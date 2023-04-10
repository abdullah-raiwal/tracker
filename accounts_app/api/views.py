from django.shortcuts import render
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView
from accounts_app.api.serializers import UserRegistartionSerialzer, UserLoginSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationView(RegisterView):

    serializer_class = UserRegistartionSerialzer

class UserLoginView(LoginView):
    
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        if response.status_code == 200:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']

            refresh = RefreshToken.for_user(user)
            
            data = {
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
                'user_id' : user.id
            }
            
            response.data = data

        return response
    
class UserLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        self.logout(request)
        return Response(status.HTTP_200_OK)