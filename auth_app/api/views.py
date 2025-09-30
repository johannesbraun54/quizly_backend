from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import CustomTokenObtainPairSerializer, RegistrationSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from ..utils import create_userprofile


@api_view(["POST"])
@permission_classes([AllowAny])
def check_email_availability(request):

    if request.method == "POST":
        email = request.data.get("email")
        if not email:
            return Response(
                {"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(email=email).exists():
            return Response({"exists": True}, status=status.HTTP_200_OK)
        else:
            return Response({"exists": False}, status=status.HTTP_200_OK)


class RegistrationView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():

            new_account = serializer.save()
            create_userprofile(new_account)

            data = {
                 "detail": "User created successfully!"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class CookieTokenObtainPairView(TokenObtainPairView):
    
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        refresh = serializer.validated_data["refresh"]
        access = serializer.validated_data["access"]
        response = Response(
            {
                "detail": "Login successful",
                "user": {
                    "id": serializer.user.id,
                    "username": serializer.user.username,
                },
            },
            status=status.HTTP_200_OK,
        )

        response.set_cookie(
            key="access_token",
            value=access,
            httponly=True,
            secure=True,
            samesite="Lax",
        )

        response.set_cookie(
            key="refresh_token",
            value=refresh,
            httponly=True,
            secure=True,
            samesite="Lax"
        )

        return response


class CookieRefreshView(TokenRefreshView):

    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get("refresh_token")

        if refresh_token is None:
            return Response(
                {"detail": "Refresh token not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.get_serializer(
            data={"refresh": refresh_token}
        )
        try:
            serializer.is_valid(raise_exception=True)
        except:
            return Response(
                {"detail": "Refresh token invalid"}, status=status.HTTP_401_UNAUTHORIZED
            )

        access_token = serializer.validated_data.get(
            "access"
        )  
        response = Response(
            {"detail": "Token refreshed", "access": access_token},
            status=status.HTTP_200_OK,
        )

        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            secure=True,
            samesite="Lax"
       )

        return response


class LogoutView(APIView):

    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get("refresh_token")

        if refresh_token == None:
            return Response({"detail": "No refresh token provided"}, status=400)

        refresh_token = RefreshToken(request.COOKIES.get("refresh_token"))
        refresh_token.blacklist()
        response = Response(
            {
                "detail": "Logout successful! All tokens will be deleted. Refresh token is now invalid."
            }
        )
        response.delete_cookie(
            key="access_token"
        )
        response.delete_cookie(
            key="refresh_token"
        )

        return response
