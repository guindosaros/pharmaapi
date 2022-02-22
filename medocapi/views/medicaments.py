from rest_framework.viewsets import ModelViewSet
from drf_yasg.utils import swagger_auto_schema


from medocapi import serializers, models, schema, filters


class MedicamentViewSet(ModelViewSet):

    serializer_class = serializers.MedicamentSerializer
    detail_serializer_class = serializers.DetailMedicamentsSerializer
    filterset_class = filters.MedicamentsFilter
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
