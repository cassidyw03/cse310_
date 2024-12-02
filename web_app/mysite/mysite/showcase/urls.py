from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='templates/portfolio'),  # Set the portfolio view
]
