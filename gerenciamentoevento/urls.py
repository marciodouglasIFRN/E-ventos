"""gerenciamentoevento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import urls as home_urls
from clientes import urls as clientes_urls
from promotor import urls as promoter_urls
from .views import register
from .views import login
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [

    # path('home/', home,name='page-home'),
    path('', include(home_urls)),
    path('clientes/', include(clientes_urls)),
    path('promoter/', include(promoter_urls)),
    path('register/', register, name='page-register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
]
