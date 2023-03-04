"""RX_DjangoNinja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from ninja import NinjaAPI, Router

# from RX.views import scientific_controller
# from account.views import api_pet
from RX.controllers.scientificController import sb_stock_controller
from account.views import account_controller

api = NinjaAPI()
api.add_router('/scientific_bureau', sb_stock_controller)
api.add_router('/account', account_controller)
# api.add_router('/signup', api_pet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('', admin.site.urls),
]
