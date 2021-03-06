from django.forms import ModelForm, ModelChoiceField
from django.utils.translation import gettext_lazy as _

from app_home.models import Application, Resume
from app_vacancy.models import Vacancy


class MySpecialtyChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.title


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['written_username', 'written_phone', 'written_cover_letter']
        labels = {
            'written_username': _('Вас зовут'),
            'written_phone': _('Ваш телефон'),
        }


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
