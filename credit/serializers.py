from rest_framework import serializers
from .models import Offer, ClientForm, CreditProposal


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('id', 'rotation_date_begin', 'rotation_date_end',
                  'offer_name', 'offer_type', 'min_score', 'max_score')


class ClientFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientForm
        fields = ('id', 'family_name', 'name', 'father_name', 'birth_date',
                  'phone_number', 'passport_number', 'score')


class BaseCreditProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditProposal
        fields = ('id', 'status')


class PartnerCreditProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditProposal
        fields = ('id', 'offer', 'client_form')


