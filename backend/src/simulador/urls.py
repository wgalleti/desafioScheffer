from rest_framework import routers

from src.simulador.api.v1.views import CenarioOperacaoViewSetV1, CenarioViewSetV1

router = routers.DefaultRouter()
router.register(r"v1/cenarios", CenarioViewSetV1)
router.register(r"v1/operacoes", CenarioOperacaoViewSetV1)

urlpatterns = router.urls
