from django.db import models
from django.conf import settings
from staff.models import Department
from npa.models import NPA


class Period(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class VisualizationType(models.Model):
    visualization_type = models.CharField(max_length=255)

    def __str__(self):
        return self.visualization_type


class Report(models.Model):
    code = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    public = models.BooleanField()
    visualization_type = models.ForeignKey(VisualizationType, on_delete=models.CASCADE)
    npa = models.ManyToManyField(NPA, blank=True)
    allowed_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return self.name


class FieldType(models.Model):
    class FormFields(models.IntegerChoices):
        BOOLEAN_FIELD = 1, 'BooleanField'
        CHAR_FIELD = 2, 'CharField'
        CHOICE_FIELD = 3, 'ChoiceField'
        TYPED_CHOICE_FIELD = 4, 'TypedChoiceField'
        DATE_FIELD = 5, 'DateField'
        DATE_TIME_FIELD = 6, 'DateTimeField'
        DECIMAL_FIELD = 7, 'DecimalField'
        DURATION_FIELD = 8, 'DurationField'
        EMAIL_FIELD = 9, 'EmailField'
        FILE_FIELD = 10, 'FileField'
        FILE_PATH_FIELD = 11, 'FilePathField'
        FLOAT_FIELD = 12, 'FloatField'
        IMAGE_FIELD = 13, 'ImageField'
        INTEGER_FIELD = 14, 'IntegerField'
        JSON_FIELD = 15, 'JSONField'
        GENERIC_IP_ADDRESS_FIELD = 16, 'GenericIPAddressField'
        MULTIPLE_CHOICE_FIELD = 17, 'MultipleChoiceField'
        TYPED_MULTIPLE_CHOICE_FIELD = 18, 'TypedMultipleChoiceField'
        NULL_BOOLEAN_FIELD = 19, 'NullBooleanField'
        REGEX_FIELD = 20, 'RegexField'
        SLUG_FIELD = 21, 'SlugField'
        TIME_FIELD = 22, 'TimeField'
        URL_FIELD = 23, 'URLField'
        UUID_FIELD = 24, 'UUIDField'

    name = models.CharField(max_length=255)
    django_form_class = models.PositiveIntegerField(choices=FormFields.choices, default=FormFields.CHAR_FIELD)
    field_config = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    national = models.CharField(max_length=255)
    world = models.CharField(max_length=255, null=True, blank=True)
    national_letter_designation = models.CharField(max_length=255)
    world_letter_designation = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class ReportField(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='fields')
    name = models.CharField(max_length=255)
    machine_name = models.SlugField(max_length=255, unique=True, null=True, default=None)
    field_type = models.ForeignKey(FieldType, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True, null=True)
    required = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['pk', ]


class ReportSnapshotStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ReportSnapshot(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(ReportSnapshotStatus, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.created_at} - {self.report}'


class ReportFieldValue(models.Model):
    report_snapshot = models.ForeignKey(ReportSnapshot, on_delete=models.CASCADE)
    field = models.ForeignKey(ReportField, on_delete=models.CASCADE)
    value = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.field} - {self.value}'
