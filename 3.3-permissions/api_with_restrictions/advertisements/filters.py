from .models import Advertisement
from django_filters import rest_framework as filters, DateFromToRangeFilter, AllValuesFilter


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = DateFromToRangeFilter()
    status = AllValuesFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']
