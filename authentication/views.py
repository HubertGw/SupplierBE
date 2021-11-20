import jwt
from django.contrib.auth import authenticate
from authentication.models import CustomUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.serializers import UserSerializer

class LoginView(APIView):
    def post(self, request, *args, **kwargs) -> Response:
        """
        Enpoint for authenticate and login user
        :param request: Pure http request
        :return: If user is authenticated and is active then returns pair of tokens (refresh,access),
         if not then 401 code will be returned
        """
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        serializer = UserSerializer(user)
        if user is not None:
            return Response(status=200, data=serializer.get_token(user))
        return Response(data={"message": "User does not exist"}, status=status.HTTP_403_FORBIDDEN)

class RegisterView(APIView):
    """
    View for registering user
    """
    model = CustomUser
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(data=user_data, status=status.HTTP_201_CREATED)
