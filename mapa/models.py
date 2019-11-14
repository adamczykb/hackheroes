from django.db import models

from django.contrib.gis.db import models as geomodels


class Point(models.Model):
    name = models.CharField(max_length=100, blank=False)
    geometry = geomodels.PointField()
    mphone = models.CharField(max_length=100)
    description=models.TextField()
    active = models.BooleanField(default=True)
    class Meta:
        # order of drop-down list items
        ordering = ('name',)

        # plural form in admin view
        verbose_name_plural = 'Punkty'