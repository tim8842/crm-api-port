from rest_framework.routers import DefaultRouter
from .views import DealView, ClientView

router = DefaultRouter()
router.register(r"clients", ClientView)
router.register(r"deals", DealView)

urlpatterns = router.urls
