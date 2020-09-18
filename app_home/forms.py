from django.forms import ModelForm

from app_home.models import Application, Company
from app_vacancy.models import Vacancy


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['written_username', 'written_phone', 'written_cover_letter']


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'logo', 'location', 'employee_count', 'description']


class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'specialty', 'salary_min', 'salary_max', 'skills', 'description']
