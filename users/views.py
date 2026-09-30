from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import RefreshToken

# Register View
class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer


#Login View
class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = User.objects.filter(
            email=email
        ).first()

        if not user:
            return Response(
                {"error": "User not found"},
                status=404
            )

        if not check_password(
            password,
            user.password
        ):
            return Response(
                {"error": "Invalid password"},
                status=400
            )
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        })

