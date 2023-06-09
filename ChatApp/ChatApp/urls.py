from django.urls import path
from .views import handle_request

urlpatterns = [
    path('endpoint/', handle_request, name='handle_request'),
]
