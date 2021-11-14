from rest_framework import mixins, viewsets

from products.models import Product
from products.serializers import ProductSerializer


class ProductView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
