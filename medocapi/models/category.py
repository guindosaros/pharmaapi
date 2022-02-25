from django.db import models


class Category(models.Model):
    nom = models.CharField(max_length=225)
    image = models.FileField(upload_to="category/", max_length=100)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"

    def __str__(self):
        return self.nom
