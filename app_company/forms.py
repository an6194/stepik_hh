from django.forms import ModelForm

from app_company.models import Company


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'logo', 'location', 'employee_count', 'description']
