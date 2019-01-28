from django.urls import path
from .views import promoter
from .views import add_new_promoter
from .views import Criar_Promotor
from .views import Listar_Promotor
# from .views import qrcode

urlpatterns = [
    path('new/', Criar_Promotor.as_view(), name="new_promotor"),
    path('list/', Listar_Promotor.as_view(), name="list_promotores"),
    path('promoter/', promoter, name="page-promoter"),
    path('newpromoter/', add_new_promoter, name="new_promotre1"),
    # path('qrcode/', qrcode, name="page-qrcode"),
]
