from django.db import models
from staff.models import Department
from npa.models import NPA


class Period(models.Model):
    name = models.CharField(max_length=255)


class VisualizationType(models.Model):
    visualization_type = models.CharField(max_length=255)


class Report(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    public = models.BooleanField()
    visualization_type = models.ForeignKey(VisualizationType, on_delete=models.CASCADE)
    npa = models.ManyToManyField(NPA)
