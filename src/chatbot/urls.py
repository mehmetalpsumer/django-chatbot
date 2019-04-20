from django.urls import path

from . import api
from . import views

urlpatterns = [
    # Views
    path('', views.index, name='index'),

    # API
    path('api/message/', api.message, name='api_message'), 
]
