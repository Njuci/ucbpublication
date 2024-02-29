from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework_jwt.utils import jwt_encode_handler,jwt_payload_handler
from .models import MyUser,Institution
#from rest_framework_jwt.authentication import authenticate
#from rest_framework_jwt.authentication import a
class SingupView_instutition(APIView):
    def post(self,request): 
        data=request.data
        serializer=UtilisateurSerial(data=data)
        if serializer.is_valid():
            serializer.save()
            id=serializer.data['id']
            institution_serializer=InstitutionSerial(data={'user':id})
            if institution_serializer.is_valid():
                institution_serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:   
                MyUser.objects.get(id=id).delete()
                return Response(institution_serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        user2=MyUser.objects.get(username=username, password=password)
        if user2 is not None:
            token = jwt_encode_handler(jwt_payload_handler(user2))
            user_type=user2.user_type
            return Response({'token': token,"user_type":user_type},status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class RefreshView(APIView):
    def post(self, request):
        token = request.data.get('token')
        if token is not None:
            try:
                user = jwt_decode_handler(token, api_settings.JWT_SECRET_KEY)
                new_token = jwt_encode_handler(jwt_payload_handler(user))
                return Response({'token': new_token})
            except:
                return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'No token provided'}, status=status.HTTP_400_BAD_REQUEST)
