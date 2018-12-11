from django.urls import path
from .views import promoter
from .views import qrcode
urlpatterns = [
    path('promoter/', promoter, name="page-promoter"),
    path('qrcode/', qrcode, name="page-qrcode"),
]
