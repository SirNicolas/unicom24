import requests
from django.test import TestCase
from rest_framework.reverse import reverse


class TestPartnerAPI(TestCase):
    api_url = 'http://127.0.0.1:8000{}'.format(reverse('client-form-list'))
    valid_headers = {
        'Authorization': 'token d52e43ed6610cde190c05f83ca79077f80f14a54'}
    invalid_headers = {
        'Authorization': 'token invalid token'}

    def test_partner_api_for_permission(self):
        r = requests.get(self.api_url, headers=self.valid_headers)
        self.assertEqual(r.status_code, 200)
        r = requests.get(self.api_url, headers=self.invalid_headers)
        self.assertEqual(r.status_code, 403)


class TestCreditOrganizationAPI(TestCase):
    api_url = 'http://127.0.0.1:8000{}'.format(reverse('credit-proposals-list'))
    valid_headers = {
        'Authorization': 'token 03175d9c3377b366c3e4d9899f68a78ac3f92621'}
    invalid_headers = {
        'Authorization': 'token invalid token'}

    def test_credit_organization_api_for_permission(self):
        r = requests.get(self.api_url, headers=self.valid_headers)
        self.assertEqual(r.status_code, 200)
        r = requests.get(self.api_url, headers=self.invalid_headers)
        self.assertEqual(r.status_code, 403)
