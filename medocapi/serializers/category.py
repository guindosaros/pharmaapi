from rest_framework.serializers import ModelSerializer
from medocapi import models


class CategorySerializer(ModelSerializer):
    """
    la Liste des category
    """

    class Meta:
        model = models.Category
        fields = "__all__"
