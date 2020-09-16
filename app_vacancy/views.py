from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from app_home.forms import ApplicationForm
from app_home.models import Application
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
        form = ApplicationForm()
        return render(request, 'vacancy.html', context={
            'vacancy': vacancy,
            'form': form
        })


class ApplicationSendView(LoginRequiredMixin, View):

    def get(self, request, vacancy_id, *args, **kwargs):
        vacancy = get_object_or_404(Vacancy, id=vacancy_id)
        try:
            Application.objects.get(vacancy=vacancy, user__id=request.user.id)
        except Application.DoesNotExist:
            return HttpResponseForbidden
        return render(request, 'sent.html', context={
            'vacancy': vacancy,
        })

    def post(self, request, vacancy_id, *args, **kwargs):
        f = ApplicationForm(request.POST).save(commit=False)
        f.vacancy = Vacancy.objects.get(id=vacancy_id)
        f.user = User.objects.get(id=request.user.id)
        f.save()
        return redirect('application_send', vacancy_id)
