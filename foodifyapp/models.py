from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django.db import models as models


class Recipe(models.Model):

    # Fields
    name = models.TextField(max_length=100)
    servings = models.IntegerField()
    ingredients = ArrayField(models.CharField(max_length=100))
    method = ArrayField(models.CharField(max_length=100))
    category = models.CharField(max_length=30)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('foodifyapp_recipe_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('foodifyapp_recipe_update', args=(self.pk,))


