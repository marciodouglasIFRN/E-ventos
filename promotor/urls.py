from django.urls import path
from .views import promoter

urlpatterns = [
    path('promoter/', promoter, name="page-promoter"),
]
