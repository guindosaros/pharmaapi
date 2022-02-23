from django.urls import reverse_lazy, reverse
from rest_framework.test import APITestCase
from medocapi.models import Medicaments


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

    def get_medicaments_list_data(self, medocs):
        return [
            {
                "id": medoc.pk,
                "code": medoc.code,
                "nom": medoc.nom,
                "ppv": medoc.ppv,
                "status": medoc.status,
                "date_add": self.format_datetime(medoc.date_add),
                "date_upd": self.format_datetime(medoc.date_upd),
            }
            for medoc in medocs
        ]

    def get_medicaments_details_data(self, medocs):
        return [
            {
                "id": medoc.pk,
                "code": medoc.code,
                "nom": medoc.nom,
                "dci1": medoc.dci1,
                "dosage1": medoc.dosage1,
                "unite_dosage1": medoc.unite_dosage1,
                "forme": medoc.forme,
                "presentation": medoc.presentation,
                "ppv": medoc.ppv,
                "ph": medoc.ph,
                "prix_br": medoc.prix_br,
                "principe_genetique": medoc.principe_genetique,
                "taux_remboursement": medoc.taux_remboursement,
                "status": medoc.status,
                "date_add": self.format_datetime(medoc.date_add),
                "date_upd": self.format_datetime(medoc.date_upd),
            }
            for medoc in medocs
        ]


class TestMedocsApi(MedocApiTestCase):
    url = reverse_lazy("medicaments-list")

    def test_list(self):
        """
        Test de verification la liste de medicaments
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(
        #     response.json()["results"],
        #     self.get_medicaments_list_data([self.medoc1, self.medoc2]),
        # )

    def test_list_filter(self):
        """
        Test de verification de recherche d'artcile par son  code
        """
        response = self.client.get(self.url + "?code=%s" % self.medoc1.code)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(
        #     self.get_medicaments_list_data([self.medoc1]), response.json()["results"]
        # )

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
        # self.assertEqual(
        #     response.json(),
        #     self.get_medicaments_details_data([self.medoc1]),
        # )
