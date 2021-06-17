from django.urls import include, path
from post.views import *

# from user import views
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', PostView.as_view(), name="post"),
    path('<pk>',PostView.as_view() , name="post"),
]