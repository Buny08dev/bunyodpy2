from django.contrib import admin
from django.urls import path,include

from bun_users.views import Registeview

urlpatterns = [
    path("",Registeview.as_view(),name="login"),]
