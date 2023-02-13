from . import views
from django.urls import path

urlpatterns = [
    path('', views.PortfolioView.as_view(), name='portfolio'),
]