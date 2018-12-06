from django.urls import path
from .views import home

urlpatterns = [
    
    path('', home, name="page-home"),
    #path('logout/', myLogout, name="logout"),
]
