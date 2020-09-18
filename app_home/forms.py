from django.forms import ModelForm, ModelChoiceField

from app_home.models import Application, Company, Resume
from app_vacancy.models import Vacancy


class MySpecialtyChoiceField(ModelChoiceField):
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
    class Meta:
        model = Vacancy
        fields = ['title', 'specialty', 'salary_min', 'salary_max', 'skills', 'description']
        field_classes = {
            'specialty': MySpecialtyChoiceField,
        }


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'surname', 'status', 'salary', 'specialty', 'grade', 'education', 'experience', 'portfolio']
        field_classes = {
            'specialty': MySpecialtyChoiceField,
        }
