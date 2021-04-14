from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core import views as vie_core


router = DefaultRouter()
router.register(r'mercados', vie_core.MarketViewSet)
router.register(r'tasas-gen', vie_core.RateGenViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
