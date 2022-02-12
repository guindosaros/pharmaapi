from drf_yasg.openapi import Response


medicament_schema = {
    "200": Response(
        description="Liste des medicaments par pages",
        examples={
            "count": 5917,
            "next": "http://127.0.0.1:8000/api/v1/medicaments/?page=2",
            "previous": "null",
            "results": [
                {
                    "id": 16558,
                    "code": "6118010000287",
                    "nom": "A-GRAM",
                    "ppv": "47.6",
                    "status": True,
                    "date_add": "2022-02-12T11:48:57.732091Z",
                    "date_upd": "2022-02-12T11:48:57.732091Z",
                },
                {
                    "id": 17231,
                    "code": "6118010000263",
                    "nom": "A-GRAM",
                    "ppv": "56.85",
                    "status": True,
                    "date_add": "2022-02-12T11:48:59.387551Z",
                    "date_upd": "2022-02-12T11:48:59.387551Z",
                },
                {
                    "id": 17555,
                    "code": "6118010000270",
                    "nom": "A-GRAM",
                    "ppv": "32.7",
                    "status": True,
                    "date_add": "2022-02-12T11:49:00.186660Z",
                    "date_upd": "2022-02-12T11:49:00.186660Z",
                },
                {
                    "id": 17458,
                    "code": "6118000010050",
                    "nom": "ABBOTICINE",
                    "ppv": "26.8",
                    "status": True,
                    "date_add": "2022-02-12T11:48:59.905795Z",
                    "date_upd": "2022-02-12T11:48:59.905795Z",
                },
                {
                    "id": 12003,
                    "code": "6118001183203",
                    "nom": "ABILIFY 10 MG",
                    "ppv": "1.5",
                    "status": True,
                    "date_add": "2022-02-12T11:48:46.031847Z",
                    "date_upd": "2022-02-12T11:48:46.031847Z",
                },
                {
                    "id": 17166,
                    "code": "6118001183210",
                    "nom": "ABILIFY 15 MG",
                    "ppv": "1.5",
                    "status": True,
                    "date_add": "2022-02-12T11:48:59.261284Z",
                    "date_upd": "2022-02-12T11:48:59.261284Z",
                },
                {
                    "id": 13075,
                    "code": "6118001170388",
                    "nom": "ACCUPRIL",
                    "ppv": "103.5",
                    "status": True,
                    "date_add": "2022-02-12T11:48:48.709557Z",
                    "date_upd": "2022-02-12T11:48:48.710562Z",
                },
                {
                    "id": 15867,
                    "code": "6118001170371",
                    "nom": "ACCUPRIL",
                    "ppv": "41.7",
                    "status": True,
                    "date_add": "2022-02-12T11:48:55.723363Z",
                    "date_upd": "2022-02-12T11:48:55.723363Z",
                },
                {
                    "id": 14033,
                    "code": "6118000130796",
                    "nom": "ACEPRIL",
                    "ppv": "98",
                    "status": True,
                    "date_add": "2022-02-12T11:48:51.406804Z",
                    "date_upd": "2022-02-12T11:48:51.407802Z",
                },
            ],
        },
    )
}

detail_medoc_schema = {
    "200": Response(
        description="Liste des medicaments par pages",
        examples={
            "application/json": [
                {
                    "id": 1,
                    "url": "https://res.cloudinary.com/leisure-experience/image/upload/v1628014350/media/organization/banners/947037_gmwerk.jpg",
                },
            ]
        },
    )
}
