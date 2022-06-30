from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import SensorView, SensorDetailView, MeasurementView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:pk>', SensorDetailView.as_view()),
    path('measurements/', MeasurementView.as_view())
]

