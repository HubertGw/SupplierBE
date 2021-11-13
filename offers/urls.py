from rest_framework.routers import SimpleRouter

from offers.views import OfferView

router = SimpleRouter()

router.register(r'', OfferView, basename='offers')

urlpatterns = router.urls
