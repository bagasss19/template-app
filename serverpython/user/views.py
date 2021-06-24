from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
from .serializers import UserSerializer, CreateUserSerializer
from .models import User

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated, AllowAny

import json
import pickle
import os

# Create your views here.
class Login(CreateAPIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is "" or password is "":
            return Response(
                {
                    'error': 'Please Input the Username and Password'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(request, username=username, password=password)
        print(user)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "key": token.key,
                "username": user.username
            })
        else :
            return Response(
            {
                'error': 'invalid username or password'
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class RegisterView(CreateAPIView):

    '''
     METHOD -> POST
     # class yang berfungsi untuk membuat akun kandidat baru.
     # hanya admin yang bisa mengakses endpoint ini.
    '''
    serializer_class = CreateUserSerializer

class UserView(CreateAPIView):
    def get(self, request):
        try:
            # return Response("ASHUPPP")
            user = User.objects.all()
            serializer = UserSerializer(user, many=True)
            return Response(serializer.data)
        except Exception as error:
            return Response({
                "detail": str(error)
            },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, pk):
        try:
            # return Response("ASHUPPP")
            user = User.objects.get(id=pk)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Exception as error:
            return Response({
                "detail": str(error)
            },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            user.delete()
            return Response("success delete!")
        except Exception as error:
            return Response({
                "detail": str(error)
            },
                status=status.HTTP_400_BAD_REQUEST,
            )

class ModelView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            module_dir = os.path.dirname(__file__)  
            tfdifloc = os.path.join(module_dir, 'tfidf.pickle')  
            mnbloc = os.path.join(module_dir, 'mnb.pickle')
            
            #Load tfidf matrix
            tfidf = pickle.load(open(tfdifloc, "rb"))

            #Load mnb model
            mnb = pickle.load(open(mnbloc, "rb"))

            tfidf_baru = tfidf.transform([request.data["word"]])
            hasil = mnb.predict(tfidf_baru)
            print(hasil, "<<<hasil nich")
            if hasil == 0:
                return Response({
                "sentiment" : "positive"
            })
            else :
                return Response({
                "sentiment" : "negative"
            })
        except Exception as error:
            return Response({
                "detail": str(error)
            },
                status=status.HTTP_400_BAD_REQUEST,
            )