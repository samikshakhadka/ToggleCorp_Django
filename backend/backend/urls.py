from backend.views import hello_geeks
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('geek/', hello_geeks),
    path('', include("model.urls"))

]
