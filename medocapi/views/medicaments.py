from ast import mod
from rest_framework.viewsets import ReadOnlyModelViewSet
from drf_yasg.utils import swagger_auto_schema
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
)

from medocapi import serializers, models, schema


class MedicamentViewSet(ReadOnlyModelViewSet):

    serializer_class = serializers.MedicamentSerializer
    detail_serializer_class = serializers.DetailMedicamentsSerializer
    lookup_field = "code"

    @swagger_auto_schema(responses=schema.medicament_schema)
    def get_queryset(self):
        """
        La liste de tous les medicaments d'une page
        """
        queryset = models.Medicaments.objects.filter(status=True)
        return queryset

    def get_serializer_class(self):
        """
        Detail d'un medicaments selectionner
        """
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()
