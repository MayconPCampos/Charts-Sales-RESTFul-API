from django.urls import path
from .views import index

app_name = "charts"
urlpatterns = [
    path("<username>", index, name="index")
]
