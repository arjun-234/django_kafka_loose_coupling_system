# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from myapp.views import register_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', register_user, name='register_user'),
]
