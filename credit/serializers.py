from rest_framework import serializers
from .models import Offer, ClientForm, CreditProposal


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('rotation_date_begin', 'rotation_date_end', 'offer_name',
                  'offer_type', 'min_score', 'max_score')


class ClientFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientForm
        fields = ('family_name', 'name', 'father_name', 'birth_date',
                  'phone_number', 'passport_number', 'score')


class CreditProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditProposal
        fields = ('id', 'offer', 'status')
