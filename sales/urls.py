from django.urls import path
from .views import SaleList, SaleDetail

app_name = "sales"
urlpatterns = [
    path("", SaleList.as_view()),
    path("<int:pk>", SaleDetail.as_view()),
]
