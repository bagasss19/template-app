from django.urls import include, path
from user.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# from user import views
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', UserView.as_view(), name="user"),
    path('model',ModelView.as_view() , name="model"),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('login', Login.as_view() , name="login"),
    path('<pk>',UserView.as_view() , name="user"),
]