from django.urls import path
from .views import ReportDetailView, get_report_details

urlpatterns = [
    path('<int:pk>/', get_report_details, name='report_detail')
]
