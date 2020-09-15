from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from app_home.models import Company
from app_vacancy.models import Specialty, Vacancy


class MainView(View):

    def get(self, request, *args, **kwargs):
        specs = Specialty.objects.all().annotate(vacancies_count=Count('vacancies'))
        companies = Company.objects.all().annotate(vacancies_count=Count('vacancies'))
        return render(request, 'index.html', context={
            'specs': specs,
            'companies': companies,
        })


class CompanyView(View):

    def get(self, request, company_id, *args, **kwargs):
        company = get_object_or_404(Company, id=company_id)
        vacancies = Vacancy.objects.filter(company=company)
        return render(request, 'company.html', context={
            'company': company,
            'vacancies': vacancies,
        })


class MyCompanyView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        try:
            company = Company.objects.get(owner=user)
        except Company.DoesNotExist:
            return render(request, 'company_create.html')
        return render(request, 'company_edit.html', context={
            'company': company,
        })


class MyVacanciesView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        try:
            company = Company.objects.get(owner=user)
        except Company.DoesNotExist:
            return redirect('my_company')
        vacancies = Vacancy.objects.filter(company=company)
        return render(request, 'my_vacancies_list.html', context={
            'vacancies': vacancies,
        })


class MyVacancyView(LoginRequiredMixin, View):

    def get(self, request, vacancy_id, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        try:
            company = Company.objects.get(owner=user)
        except Company.DoesNotExist:
            return redirect('my_company')
        try:
            vacancy = Vacancy.objects.get(company=company, id=vacancy_id)
        except Vacancy.DoesNotExist:
            return redirect('my_vacancies')
        return render(request, 'vacancy_edit.html', context={
            'vacancy': vacancy,
        })


def custom_handler404(request, exception):
    return HttpResponseNotFound('Похоже Вы заблудились...')


def custom_handler500(request):
    return HttpResponseServerError('Надо мастера звать - пусть чинит.')
