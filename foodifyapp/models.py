from django.urls import reverse
from django.db.models import BigAutoField
from django.db.models import TextField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models


class DaysOfTheWeek(models.Model):

    # Fields
    day = models.TextField(max_length=100)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('foodifyapp_daysoftheweek_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('foodifyapp_daysoftheweek_update', args=(self.pk,))

class new_days(models.Model):

    # Fields
    title = models.CharField(max_length=255)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('foodifyapp_days_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('foodifyapp_days_update', args=(self.pk,))

