from django.test import TestCase
from model_bakery import baker
from rest_framework.reverse import reverse

from products.serializers import ProductSerializer


class ProductViewTest(TestCase):

    def setUp(self) -> None:
        self.product_1 = baker.make('Product')
        self.product_2 = baker.make('Product')
        self.product_list_url = reverse('products-list')
        self.product_detail_url = reverse('products-detail', args=[self.product_1.id])

    def test_should_return_product_list(self):
        # when
        response = self.client.get(self.product_list_url)
        # then
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_should_return_product(self):
        # when
        response = self.client.get(self.product_detail_url)
        # then
        serializer_data = ProductSerializer(instance=self.product_1).data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer_data)
