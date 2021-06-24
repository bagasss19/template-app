from django.urls import include, path
from user.views import *

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', UserView.as_view(), name="user"),
    path('register', RegisterView.as_view(), name="register"),
    path('model',ModelView.as_view() , name="model"),
    path('login', Login.as_view() , name="login"),
    path('<pk>',UserView.as_view() , name="user"),
]