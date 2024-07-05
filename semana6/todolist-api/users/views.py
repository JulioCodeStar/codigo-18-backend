from .models import User
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password

# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class AuthenticationView(APIView):
    def post(self, request):
        # request.data = es la informacion que recibimos del cliente
        user_request = UserLoginSerializer(data=request.data)
        
        if not user_request.is_valid():
            return Response({
                "message: ": "Email y/o password incorrecto"
            }, status=401)

        # buscar el usuario por correo
        user = User.objects.get(email=user_request.data['email'])

        if not user:
            return Response({
                "message: ": "El email no existe"
            }, status=401)
        
        user_serializer = UserSerializer(user).data
        # comparar que el password sea correcto
        if check_password(user_request.data['password'], user_serializer):
            return Response({
                "message: ": "Email y/o password incorrectos"
            }, status=401)
        
        return Response({"message": "Todo bien"})