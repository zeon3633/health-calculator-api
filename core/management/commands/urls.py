from django.urls import path
from .views import CalculateHealthMetricsView, CalculationHistoryListView

urlpatterns = [
    path('calculate/', CalculateHealthMetricsView.as_view(), name='calculate'),
    path('history/', CalculationHistoryListView.as_view(), name='history'),
]