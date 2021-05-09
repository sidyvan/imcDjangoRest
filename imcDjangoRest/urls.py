from django.contrib import admin
from django.urls import path

from imc.views import ImcPost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ImcPost.as_view()),
]
