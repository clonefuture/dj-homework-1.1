from django_filters import DateFromToRangeFilter, AllValuesFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet

from .permissions import IsOwnerOrReadOnly
from .models import Advertisement
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import AdvertisementSerializer


class FilterData(FilterSet):
    created_at = DateFromToRangeFilter()
    status = AllValuesFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FilterData

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", 'destroy']:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []

