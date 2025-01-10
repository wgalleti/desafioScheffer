from rest_framework import routers

from src.base.api.v1.views import AlgodoeiraViewSetV1, FazendaViewSetV1, UserViewSetV1

router = routers.DefaultRouter()
router.register(r"v1/users", UserViewSetV1)
router.register(r"v1/algodoeiras", AlgodoeiraViewSetV1)
router.register(r"v1/fazendas", FazendaViewSetV1)

urlpatterns = router.urls
