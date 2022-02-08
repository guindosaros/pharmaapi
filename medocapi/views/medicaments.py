from ast import mod
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from medocapi import serializers, models
from django.shortcuts import get_object_or_404
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
)


class MedicamentViewSet(ReadOnlyModelViewSet):
    serializer_class = serializers.MedicamentSerializer
    detail_serializer_class = serializers.DetailMedicamentsSerializer

    def get_queryset(self):
        queryset = models.Medicaments.objects.filter(status=True)
        return queryset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()
