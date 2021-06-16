from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
from .serializers import UserSerializer, UserLoginSerializer
from .models import User

from nltk.sentiment import SentimentIntensityAnalyzer

# Create your views here.
class Login(CreateAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        # return Response("ASHUPPPPPPPP")
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
            }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

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

    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
    def post(self, request):
        try:
            sia = SentimentIntensityAnalyzer()
            result = sia.polarity_scores(request.data["word"])
            print(result)

            if result["compound"] > 0:
                return Response({
                "compound score": result["compound"],
                "sentiment" : "positive"
            })
            else :
                return Response({
                "compound score": result["compound"],
                "sentiment" : "negative"
            })
        except Exception as error:
            return Response({
                "detail": str(error)
            },
                status=status.HTTP_400_BAD_REQUEST,
            )