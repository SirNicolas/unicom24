from django.conf.urls import url
from rest_framework.documentation import include_docs_urls

from . import views

urlpatterns = [
    url('^', include_docs_urls(title='credit API')),
    url(r'^api/client-forms/$', views.ClientFormList.as_view(),
        name='client-form-list'),
    url(r'^api/client-forms-create/$', views.ClientFormCreate.as_view(),
        name='client-form-create'),
    url(r'^api/credit-proposal-create/$', views.CreditProposalCreate.as_view(),
        name='credit-proposal-create'),
    url(r'^api/client-forms/(?P<pk>[0-9]+)/$', views.ClientFormDetail.as_view(),
        name='client-form-detail'),
    url(r'^api/credit-proposals/(?P<pk>[0-9]+)/$',
        views.CreditProposalDetail.as_view(),
        name='credit-proposals-detail'),
    url(r'^api/credit-proposals/$', views.CreditProposalList.as_view(),
        name='credit-proposals-list'),
    url(r'^api/offers/$', views.OfferList.as_view(),
        name='offers-list'),
]
