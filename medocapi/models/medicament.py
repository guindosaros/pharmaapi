from django.db import models


class Medicaments(models.Model):
    """Model definition for Medicaments."""

    code = models.CharField(max_length=225)
    nom = models.CharField(max_length=225)
    dci1 = models.CharField(max_length=225)
    dosage1 = models.CharField(max_length=225)
    unite_dosage1 = models.CharField(max_length=225)
    forme = models.CharField(max_length=225)
    presentation = models.CharField(max_length=225)
    ppv = models.CharField(max_length=225)
    ph = models.CharField(max_length=225)
    prix_br = models.CharField(max_length=225)
    principe_genetique = models.CharField(max_length=225)
    taux_remboursement = models.CharField(max_length=225)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Medicaments."""

        verbose_name = "Medicaments"
        verbose_name_plural = "Medicamentss"
        ordering = ("nom",)

    def __str__(self):
        """Unicode representation of Medicaments."""
        return self.nom
