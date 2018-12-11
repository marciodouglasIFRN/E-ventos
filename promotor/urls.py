from django.urls import path
from .views import promoter
from .views import add_new_promoter

urlpatterns = [
    path('promoter/', promoter, name="page-promoter"),
    path('newpromoter/', add_new_promoter, name="new_promotre"),
    path('qrcode/', qrcode, name="page-qrcode"),
]
