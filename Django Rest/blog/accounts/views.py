from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT,
)
from .models import User
from .serializers import UserSerializer

login = obtain_auth_token


class Logout(APIView):
    """
    Delete user's authtoken
    """

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response(
            data={"message": f"Bye {request.user.username}!"},
            status=HTTP_204_NO_CONTENT,
        )


class Register(CreateAPIView):
    """
    Create a new user.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            user = serializer.instance
            return Response(
                data={
                    "id": user.id,
                    "username": user.username,
                },
                status=HTTP_201_CREATED,
            )
        return Response({"message": serializer.errors}, status=HTTP_400_BAD_REQUEST)
