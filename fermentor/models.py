from django.db import models


class TargetTemperature(models.Model):
    """A temperature target for a sensor."""
    # The sensor where this temperature target is to be applied.
    sensor = models.ForeignKey(Sensor)
    # The time that the target temperature should be hit.
    timestamp = models.DateTimeField(null=True, blank=True)
    # The target temperature.
    temperature = models.DecimalField(max_digits=5, decimal_places=5)


class MeasuredTemperature(models.Model):
    """A temperature measurement taken at a sensor at a particular time."""
    sensor = models.ForeignKey(Sensor)
    timestamp = models.DateTimeField()
    temperature = models.DecimalField(max_digits=5, decimal_places=5)


class Sensor(models.Model):
    uid = models.CharField()
    label = models.CharField()
