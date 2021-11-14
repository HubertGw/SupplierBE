from rest_framework.routers import SimpleRouter

from products.views import ProductView

router = SimpleRouter()

router.register(r'', ProductView, basename='products')

urlpatterns = router.urls
