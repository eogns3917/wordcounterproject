
from django.contrib import admin
from django.urls import path,include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("helloworld.urls")),
    path('example/',include("secondapp.urls")),
    path('login/',include("login.urls")),
]
