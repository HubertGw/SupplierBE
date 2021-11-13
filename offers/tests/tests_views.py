from django.test import TestCase
from model_bakery import baker
from rest_framework.reverse import reverse

from offers.serializers import OfferSerializer


class OfferViewTest(TestCase):

    def setUp(self) -> None:
        self.offer_1 = baker.make('Offer')
        self.offer_2 = baker.make('Offer')
        self.offers_list_url = reverse('offers-list')
        self.offers_detail_url = reverse('offers-detail', args=[self.offer_1.id])

    def test_should_return_offer_list(self):
        # when
        response = self.client.get(self.offers_list_url)
        # then
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_should_return_offer(self):
        # when
        response = self.client.get(self.offers_detail_url)
        # then
        serializer_data = OfferSerializer(instance=self.offer_1).data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer_data)
