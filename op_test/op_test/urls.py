from django.contrib import admin
from django.urls import path

from api.views import create_document

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', create_document)
]
