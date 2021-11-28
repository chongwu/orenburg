from django.shortcuts import render
from django.views.generic import DetailView
from django import forms
from .models import Report


class ReportForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)

        report = self.instance
        for field in report.fields.all():
            attr = {
                'required': field.required,
                'label': field.name
            }
            field_type = field.field_type.get_django_form_class_display()
            if field_type == 'DateField':
                attr['widget'] = forms.DateInput(attrs={'type': 'date'})
            self.fields[field.machine_name] = getattr(forms, field_type)(**attr)

    class Meta:
        model = Report
        fields = []


def get_report_details(request, pk):
    report = Report.objects.get(pk=pk)
    form = ReportForm(instance=report)
    return render(request, 'report/detail.html', {'form': form})


class ReportDetailView(DetailView):
    model = Report
    form = ReportForm
    template_name = 'report/detail.html'
