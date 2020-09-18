from django.forms import ModelForm, ModelChoiceField

from app_home.models import Application, Company
from app_vacancy.models import Vacancy, Specialty


class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.title


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['written_username', 'written_phone', 'written_cover_letter']


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'logo', 'location', 'employee_count', 'description']


class VacancyForm(ModelForm):
    specialty = MyModelChoiceField(queryset=Specialty.objects.all(), empty_label=None, label='Специальность')

    class Meta:
        model = Vacancy
        fields = ['title', 'specialty', 'salary_min', 'salary_max', 'skills', 'description']
