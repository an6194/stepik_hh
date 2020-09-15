from django.shortcuts import render, get_object_or_404
from django.views import View

from app_vacancy.models import Specialty, Vacancy


class VacanciesView(View):

    def get(self, request, *args, **kwargs):
        spec = 'Все вакансии'
        vacancies = Vacancy.objects.all()
        return render(request, 'vacancies.html', context={
            'spec': spec,
            'vacancies': vacancies,
        })


class VacanciesBySpecView(View):

    def get(self, request, spec, *args, **kwargs):
        spec = get_object_or_404(Specialty, code=spec)
        vacancies = Vacancy.objects.filter(specialty=spec)
        spec = spec.title
        return render(request, 'vacancies.html', context={
            'spec': spec,
            'vacancies': vacancies,
        })


class VacancyView(View):

    def get(self, request, vacancy_id, *args, **kwargs):
        vacancy = get_object_or_404(Vacancy, id=vacancy_id)
        return render(request, 'vacancy.html', context={
            'vacancy': vacancy
        })


class ApplicationSendView(View):

    def get(self, request, vacancy_id, *args, **kwargs):
        vacancy = get_object_or_404(Vacancy, id=vacancy_id)
        return render(request, 'sent.html', context={
            'vacancy': vacancy,
        })
