from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from authentication.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password', 'username']
        read_only_fields = ('id',)
        extra_kwargs = {'password': {'write_only': True}, 'email': {'required': True}}

    def validate_email(self, email:str):
        """
        Validates the registration of a new user
        :param data: dict in format
        {
            'email': 'some_email',
            'password': 'some_password',
            'username':'some_username'
        }
        :return: Data if valid, othwerwise raises a validation exception.
        """
        if len(email) == 0:
            raise serializers.ValidationError('Email is required.')
        if CustomUser.objects.filter(email=email):
            raise serializers.ValidationError('A user with that email already exists.')
        return email

    def get_token(self, user: CustomUser) -> dict[str, str]:
        """
        Returns new pair of tokens (refresh,access)
        :param user: Object of user for whom token has to be got
        :return: Pair of tokens (refresh,access)
        """
        refresh = UserToken.get_token(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def create(self, validated_data: dict) -> CustomUser:
        """
        Creates a new user
        :param validated_data: Data to create user (email,username,password) in following format
        {
        'email':'some email',
        'username':'some username',
        'password':'some password',
        }
        :return: created User if was created successfully
        """
        return CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password(validated_data['password']),
            is_active=False
        )

class UserToken(TokenObtainPairSerializer):
    """
    Class for customizing default JWT token
    """

    @classmethod
    def get_token(cls, user: CustomUser) -> RefreshToken:
        """
        :rtype: dict[str, str]
        :param user: Object of user for whom token has to be got
        :return: Pair of customized tokens (refresh,access)
        {
            "token_type": "token_type",
            "exp": 9_digit_expiration_time,
            "jti": "secret_jti",
            "user_id": user_id,
            "username": "username",
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email",
        }
        """
        token = super().get_token(user)
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        return token