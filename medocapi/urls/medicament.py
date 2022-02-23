from rest_framework import routers
from medocapi import views
from django.urls import path, include

# Ici nous créons notre routeur
router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register("medicaments", views.MedicamentViewSet, basename="medicaments")
BASE_PATH = "api/v1"

urlpatterns = [
    path("", views.page_principale, name="index"),
    path("detail-medoc/<str:code>", views.detail_page, name="detail"),
    path(f"{BASE_PATH}/", include(router.urls)),
]
