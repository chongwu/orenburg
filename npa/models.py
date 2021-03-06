from django.db import models


class NPAType(models.Model):
    npa_type = models.CharField(max_length=255)

    def __str__(self):
        return self.npa_type


class NPA(models.Model):
    name = models.CharField(max_length=255)
    number = models.PositiveIntegerField()
    date = models.DateField()
    npa_type = models.ForeignKey(NPAType, on_delete=models.CASCADE)
    npa_file = models.FileField(upload_to='npa/', blank=True, null=True)

    def __str__(self):
        return self.name
