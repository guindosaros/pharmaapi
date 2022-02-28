from django.urls import reverse_lazy, reverse
from rest_framework.test import APITestCase
from medocapi.models import Medicaments, Category
from django.core.files.uploadedfile import SimpleUploadedFile


DATAS = [
    {
        "code": "6118010000287",
        "nom": "A-GRAM",
        "dci1": "AMOXICILLINE",
        "dosage1": "500",
        "unite_dosage1": "MG",
        "forme": "POUDRE POUR SUSPENSION BUVABLE",
        "presentation": "1 FLACON 60 ML",
        "ppv": "47.6",
        "ph": " 31.50   ",
        "prix_br": "47.6",
        "principe_genetique": "G",
        "taux_remboursement": "70%",
        "date_add": "2022-02-12T11:48:57.732091Z",
        "date_upd": "2022-02-12T11:48:57.732091Z",
    },
    {
        "code": "6118010000270",
        "nom": "A-GRAM",
        "dci1": "AMOXICILLINE",
        "dosage1": "250",
        "unite_dosage1": "MG",
        "forme": "POUDRE POUR SUSPENSION BUVABLE",
        "presentation": "1 FLACON 60 ML",
        "ppv": "32.7",
        "ph": " 21.60   ",
        "prix_br": "32.7",
        "principe_genetique": "G",
        "taux_remboursement": "70%",
        "date_add": "2022-02-12T11:49:00.186660Z",
        "date_upd": "2022-02-12T11:49:00.186660Z",
    },
    {
        "code": "6118000270102",
        "nom": "ACIDE DEXTROSE EM 80 D2",
        "dci1": "CONCENTRE POUR HEMODIALYSE",
        "dosage1": "",
        "unite_dosage1": "NA",
        "forme": "SOLUTE CONCENTRE",
        "presentation": "1 BIDON 5 L",
        "ppv": "80",
        "ph": " 50.00   ",
        "prix_br": "80",
        "principe_genetique": "G",
        "taux_remboursement": "70%",
    },
]

image1 = SimpleUploadedFile(name="sample.jpg", content=b"", content_type="image/jpeg")
image2 = SimpleUploadedFile(name="sample2.jpg", content=b"", content_type="image/jpeg")


class MedocApiTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.medoc1 = Medicaments.objects.create(
            code=DATAS[0]["code"],
            nom=DATAS[0]["nom"],
            dci1=DATAS[0]["dci1"],
            dosage1=DATAS[0]["dosage1"],
            unite_dosage1=DATAS[0]["unite_dosage1"],
            forme=DATAS[0]["forme"],
            presentation=DATAS[0]["presentation"],
            ppv=DATAS[0]["ppv"],
            ph=DATAS[0]["ph"],
            prix_br=DATAS[0]["prix_br"],
            principe_genetique=DATAS[0]["principe_genetique"],
            taux_remboursement=DATAS[0]["taux_remboursement"],
        )
        cls.medoc2 = Medicaments.objects.create(
            code=DATAS[1]["code"],
            nom=DATAS[1]["nom"],
            dci1=DATAS[1]["dci1"],
            dosage1=DATAS[1]["dosage1"],
            unite_dosage1=DATAS[1]["unite_dosage1"],
            forme=DATAS[1]["forme"],
            presentation=DATAS[1]["presentation"],
            ppv=DATAS[1]["ppv"],
            ph=DATAS[1]["ph"],
            prix_br=DATAS[1]["prix_br"],
            principe_genetique=DATAS[1]["principe_genetique"],
            taux_remboursement=DATAS[1]["taux_remboursement"],
        )

    def format_datetime(self, value):
        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


class CategoryApiTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category1: Category = Category.objects.create(
            nom="Category1", image=image1, status=True
        )

        cls.category2: Category = Category.objects.create(
            nom="Category2", image=image2, status=True
        )


class TestMedocsApi(MedocApiTestCase):
    url = reverse_lazy("medicaments-list")

    def test_list(self):
        """
        Test de verification la liste de medicaments
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_list_filter(self):
        """
        Test de verification de recherche d'artcile par son  code
        """
        response = self.client.get(self.url + "?code=%s" % self.medoc1.code)
        self.assertEqual(response.status_code, 200)

    def test_introuvable_details_medicaments(self):
        """
        Test de verification d'une page introuvable
        """
        response = self.client.get(reverse("medicaments-detail", kwargs={"code": 444}))
        self.assertEqual(response.status_code, 404)

    def test_details_medicaments(self):
        """
        Test de verification d'une page de details de medicament
        """
        response = self.client.get(
            reverse("medicaments-detail", kwargs={"code": self.medoc1.code})
        )
        self.assertEqual(response.status_code, 200)

    def test_create_medicaments(self):
        Medoc_count = Medicaments.objects.count()
        response = self.client.post(
            self.url,
            data={
                "code": "Nouvelle catégorie",
                "nom": "Test",
                "dci1": "dci1",
                "dosage1": "dosage1",
                "unite_dosage1": "unite_dosage1",
                "forme": "forme",
                "presentation": "presentation",
                "ppv": "ppv",
                "ph": "ph",
                "prix_br": "prix_br",
                "principe_genetique": "principe_genetique",
                "taux_remboursement": "taux_remboursement",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Medicaments.objects.count(), Medoc_count + 1)

    def test_delette_medicaments(self):
        response = self.client.delete(
            reverse("medicaments-detail", kwargs={"code": self.medoc1.code})
        )
        self.assertEqual(response.status_code, 204)


class TestCategoryAPi(CategoryApiTestCase):
    url = reverse_lazy("category-list")

    def test_list_category(self):
        """
        Test de verification la liste de medicaments
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
