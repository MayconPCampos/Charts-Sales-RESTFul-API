from django.urls import path
from .views import Users

app_name = "account"
urlpatterns = [
    path("", Users.as_view())
]