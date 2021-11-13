from rest_framework import mixins, viewsets

from offers.models import Offer
from offers.serializers import OfferSerializer


class OfferView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
