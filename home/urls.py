from django.urls import path
# from .views import home
from .views import about
from .views import MyHome
urlpatterns = [

    # path('', home, name="page-home"),
    path('', MyHome.as_view(), name="page-home"),
    path('about/', about, name='page-about'),
    #path('logout/', myLogout, name="logout"),
]
