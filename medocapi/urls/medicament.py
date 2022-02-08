from rest_framework import routers
from medocapi import views
from django.urls import path, include

# Ici nous créons notre routeur
router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register("medicaments", views.MedicamentViewSet, basename="medicaments")


urlpatterns = [
    path("", include(router.urls)),
]
