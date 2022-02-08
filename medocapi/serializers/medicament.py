from rest_framework.serializers import ModelSerializer
from medocapi import models


class MedicamentSerializer(ModelSerializer):
    class Meta:
        model = models.Medicaments
        fields = ("code", "nom", "ppv", "status", "date_add", "date_upd")


class DetailMedicamentsSerializer(ModelSerializer):
    class Meta:
        model = models.Medicaments
        fields = "__all__"
