from django.urls import path
from .views import home
from .views import about

urlpatterns = [

    path('', home, name="page-home"),
    path('about/', about, name='page-about'),
    #path('logout/', myLogout, name="logout"),
]
