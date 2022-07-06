# from rest_framework.routers import DefaultRouter
from django.urls import path
# from advertisements import views
from advertisements.views import AdvertisementViewSet

# router = DefaultRouter()
# router.register('adv', views.AdvertisementViewSet)

urlpatterns = [
    path('advertisements/', AdvertisementViewSet),

]