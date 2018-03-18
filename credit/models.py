from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class BaseTimeModel(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    date_changed = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UserProfile(models.Model):
    is_credit_organization = models.BooleanField(
        verbose_name='Кредитная организация', default=False)
    is_partner = models.BooleanField(verbose_name='Партнер', default=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile', null=True)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователя'


class Offer(BaseTimeModel):
    CONSUMER_CREDIT = 1
    MORTGAGE = 2
    AUTO_CREDIT = 3
    CREDIT_TYPE = (
        (CONSUMER_CREDIT, 'потредительский кредит'),
        (MORTGAGE, 'ипотека'),
        (AUTO_CREDIT, 'автокредит'),
    )

    rotation_date_begin = models.DateTimeField()
    rotation_date_end = models.DateTimeField()
    offer_name = models.CharField(max_length=250)
    offer_type = models.PositiveSmallIntegerField(
        CREDIT_TYPE, default=CONSUMER_CREDIT)
    min_score = models.PositiveSmallIntegerField(default=0)
    max_score = models.PositiveSmallIntegerField(default=0)
    credit_organization = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Кредитная организация',
        limit_choices_to={'profile__is_credit_organization': True}, null=True)

    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'

    def get_offer_type(self):
        return Offer.CREDIT_TYPE[self.offer_type]

    def __str__(self):
        return '{} - {}'.format(self.offer_name, self.get_offer_type())


class ClientForm(BaseTimeModel):
    family_name = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    father_name = models.CharField(max_length=250)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=12)
    passport_number = models.CharField(max_length=10)
    score = models.PositiveSmallIntegerField(default=0)
    partner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Партнер',
        limit_choices_to={'profile__is_partner': True}, null=True)

    class Meta:
        verbose_name = 'Анкета клиента'
        verbose_name_plural = 'Анкеты клиентов'

    def get_fio(self):
        return '{} {} {}'.format(self.family_name, self.name, self.family_name)

    def __str__(self):
        return self.get_fio()


class CreditProposal(models.Model):
    NEW = 1
    SENT = 2
    RECEIVED = 3
    APPROVED = 4
    DECLINED = 5
    DONE = 6
    CREDIT_STATUS = (
        (NEW, 'новая'),
        (SENT, 'отправлена'),
        (RECEIVED, 'получена'),
        (APPROVED, 'одобрена'),
        (DECLINED, 'отказано'),
        (DONE, 'выдано'),
    )

    date_created = models.DateTimeField(auto_now=True)
    date_sent = models.DateTimeField(null=True)
    status = models.PositiveSmallIntegerField(
        CREDIT_STATUS, default=NEW)
    offer = models.ForeignKey(
        Offer, on_delete=models.CASCADE, null=True, verbose_name='Предложение')
    client_form = models.ForeignKey(
        ClientForm, on_delete=models.CASCADE, null=True,
        verbose_name='Анкета клиента')

    class Meta:
        verbose_name = 'Заявка в кредитную организацию'
        verbose_name_plural = 'Заявки в кредитные организации'

    def get_status(self):
        return CreditProposal.CREDIT_STATUS[self.status]

    def __str__(self):
        return '{} {} {}'.format(self.client_form.get_fio(),
                                 self.offer.offer_name,
                                 self.get_status())


# созданим API-токен для нового пользователя
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    profiles = UserProfile.objects.filter(user=instance)
    if not profiles.exists() and not instance.profile:
        UserProfile.objects.create(user=instance)
