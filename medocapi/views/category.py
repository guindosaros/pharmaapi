from rest_framework.viewsets import ModelViewSet
from medocapi import serializers, models


class CategoryViewSet(ModelViewSet):

    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        """
        La liste de tous les category
        """
        queryset = models.Category.objects.filter(status=True)
        return queryset

    def get_serializer_class(self):
        """
        Detail d'un d'une category
        """
        if self.action == "retrieve":
            return self.serializer_class
        return super().get_serializer_class()
