from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Offer
from .serializers import OfferSerializer

# Create your views here.

def home_widok(*args, **kwargs):
    return HttpResponse("<h1>Hello world!</h1>")


@api_view(['GET'])
def offer_list(request):
    offers = Offer.objects.all()
    serializer = OfferSerializer(offers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def offer_detail(request, pk):
    offers = Offer.objects.get(id=pk)
    serializer = OfferSerializer(offers, many=False)
    return Response(serializer.data)