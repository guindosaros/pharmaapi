from rest_framework.serializers import ModelSerializer
from medocapi import models


class MedicamentSerializer(ModelSerializer):
    """
    la Liste de toutes les medicaments par page
    """

    class Meta:
        model = models.Medicaments
        fields = "__all__"
        # fields = ("id", "code", "nom", "ppv", "status", "date_add", "date_upd")
        lookup_field = "code"


class DetailMedicamentsSerializer(ModelSerializer):
    class Meta:
        model = models.Medicaments
        fields = "__all__"
