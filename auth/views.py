from django.contrib.auth import login, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from auth.serializers import LoginSerializer
from rest_framework import status
# Create your views here.

class Login(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'message':'Login Successful!'}, status=status.HTTP_200_OK)
        else:
            return Response({'error':'Invalid Credentials!'}, status=status.HTTP_400_BAD_REQUEST)