from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from .serializers import ClientFormSerializer, CreditProposalSerializer
from .models import ClientForm, CreditProposal
from .permissions import PartnerPermission, CreditOrganizationPermission


class ClientFormList(generics.ListCreateAPIView):
    serializer_class = ClientFormSerializer
    queryset = ClientForm.objects.all()
    permission_classes = (PartnerPermission,)
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = '__all__'
    ordering_fields = '__all__'


class ClientFormDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ClientFormSerializer
    queryset = ClientForm.objects.all()
    permission_classes = (PartnerPermission,)


class CreditProposalList(generics.ListAPIView):
    serializer_class = CreditProposalSerializer
    queryset = CreditProposal.objects.all()
    permission_classes = (CreditOrganizationPermission,)
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = '__all__'
    ordering_fields = '__all__'


class CreditProposalDetail(generics.RetrieveAPIView):
    serializer_class = CreditProposalSerializer
    queryset = CreditProposal.objects.all()
    permission_classes = (CreditOrganizationPermission,)
