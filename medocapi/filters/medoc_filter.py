import django_filters
from medocapi import models


class MedicamentsFilter(django_filters.FilterSet):

    nom = django_filters.CharFilter(lookup_expr="icontains")
    code = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = models.Medicaments
        fields = []
