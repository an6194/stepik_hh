from django.http import Http404
from django.shortcuts import render
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
        try:
            spec = Specialty.objects.get(code=spec)
        except Specialty.DoesNotExist:
            raise Http404
        vacancies = Vacancy.objects.filter(specialty=spec)
        spec = spec.title
        return render(request, 'vacancies.html', context={
            'spec': spec,
            'vacancies': vacancies,
        })


class VacancyView(View):

    def get(self, request, vacancy_id, *args, **kwargs):
        try:
            vacancy = Vacancy.objects.get(id=vacancy_id)
        except Vacancy.DoesNotExist:
            raise Http404
        return render(request, 'vacancy.html', context={
            'vacancy': vacancy
        })
