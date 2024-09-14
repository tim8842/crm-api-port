from rest_framework import viewsets
from .models import Client, Deal
from .serializers import ClientSerializer, DealSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import api_view


class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["city", "last_contact_date"]


class DealView(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer


@api_view(["GET"])
def deals_report(request):
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")
    deals_count = Deal.objects.filter(
        deal_date__range=[start_date, end_date]
    ).count()
    return Response({"deals_count": deals_count})
