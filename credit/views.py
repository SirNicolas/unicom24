from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from .serializers import ClientFormSerializer, OfferSerializer, \
    PartnerCreditProposalSerializer, BaseCreditProposalSerializer
from .models import ClientForm, CreditProposal, Offer
from .permissions import PartnerPermission, CreditOrganizationPermission


# Партнерское API
class ClientFormList(generics.ListCreateAPIView):
    serializer_class = ClientFormSerializer
    permission_classes = (PartnerPermission,)
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = '__all__'
    ordering_fields = '__all__'

    def get_queryset(self):
        user = self.request.user
        return ClientForm.objects.filter(partner=user)


class ClientFormDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ClientFormSerializer
    permission_classes = (PartnerPermission,)

    def get_queryset(self):
        user = self.request.user
        return ClientForm.objects.filter(partner=user)


class ClientFormCreate(generics.CreateAPIView):
    serializer_class = ClientFormSerializer
    permission_classes = (PartnerPermission,)

    def get_queryset(self):
        user = self.request.user
        return ClientForm.objects.filter(partner=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(partner=user)


class CreditProposalCreate(generics.CreateAPIView):
    serializer_class = PartnerCreditProposalSerializer
    permission_classes = (PartnerPermission,)
    queryset = CreditProposal.objects.all()


class OfferList(generics.ListAPIView):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()
    permission_classes = (PartnerPermission,)
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = '__all__'
    ordering_fields = '__all__'


# API кредитных организаций
class CreditProposalList(generics.ListAPIView):
    serializer_class = BaseCreditProposalSerializer
    permission_classes = (CreditOrganizationPermission,)
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = '__all__'
    ordering_fields = '__all__'

    def get_queryset(self):
        user = self.request.user
        return CreditProposal.objects.filter(offer__credit_organization=user)


class CreditProposalDetail(generics.RetrieveUpdateAPIView):
    serializer_class = BaseCreditProposalSerializer
    permission_classes = (CreditOrganizationPermission,)

    def get_queryset(self):
        user = self.request.user
        return CreditProposal.objects.filter(offer__credit_organization=user)
