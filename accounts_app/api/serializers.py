from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from django.contrib.auth.models import User


class UserRegistartionSerialzer(RegisterSerializer):

    class Meta:
        model = User
        fields = "__all__"


class UserLoginSerializer(LoginSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('email')

    class Meta:
        model = User
        fields = ["username", "password"]

