from rest_framework import mixins, viewsets
from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer


class CategoryView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
