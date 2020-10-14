from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from app_company.forms import CompanyForm
from app_company.models import Company
from app_home.forms import VacancyForm
from app_home.models import Application
from app_vacancy.models import Vacancy


class MyCompanyView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        try:
            company = request.user.company
        except Company.DoesNotExist:
            return render(request, 'company_create.html')
        form = CompanyForm(instance=company)
        return render(request, 'company_edit.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        try:
            company = request.user.company
        except Company.DoesNotExist:
            return render(request, 'company_create.html')
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Информация о компании обновлена')
            return redirect('my_company')
        return render(request, 'company_edit.html', context={
            'form': form,
        })


class CreateCompanyView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(request, 'company_edit.html', context={
            'form': CompanyForm(),
        })

    def post(self, request, *args, **kwargs):
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            new_company = form.save(commit=False)
            new_company.owner = request.user
            new_company.save()
            messages.add_message(request, messages.SUCCESS, 'Ваша компания успешно создана!')
            return redirect('my_company')
        return render(request, 'company_edit.html', context={
            'form': form,
        })


class MyVacanciesView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        try:
            company = request.user.company
        except Company.DoesNotExist:
            return redirect('my_company')
        vacancies = Vacancy.objects.filter(company=company).annotate(applications_count=Count('applications'))
        return render(request, 'my_vacancies_list.html', context={
            'vacancies': vacancies,
        })


class CreateVacancyView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        try:
            request.user.company
        except Company.DoesNotExist:
            return redirect('my_company')
        form = VacancyForm()
        return render(request, 'vacancy_edit.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        try:
            company = request.user.company
        except Company.DoesNotExist:
            return redirect('my_company')
        form = VacancyForm(request.POST)
        if form.is_valid():
            new_vacancy = form.save(commit=False)
            new_vacancy.company = company
            new_vacancy.save()
            return redirect('my_vacancies')
        return render(request, 'vacancy_edit.html', context={
            'form': form,
        })


class MyVacancyView(LoginRequiredMixin, View):

    def get(self, request, vacancy_id, *args, **kwargs):
        try:
            company = request.user.company
        except Company.DoesNotExist:
            return redirect('my_company')
        vacancy = get_object_or_404(Vacancy, company=company, id=vacancy_id)
        form = VacancyForm(instance=vacancy)
        applications = Application.objects.filter(vacancy__id=vacancy_id)
        return render(request, 'vacancy_edit.html', context={
            'form': form,
            'applications': applications,
        })

    def post(self, request, vacancy_id, *args, **kwargs):
        try:
            company = request.user.company
        except Company.DoesNotExist:
            return redirect('my_company')
        try:
            vacancy = Vacancy.objects.get(company=company, id=vacancy_id)
        except Vacancy.DoesNotExist:
            return redirect('my_vacancies')
        form = VacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Вакансия обновлена')
            return redirect('my_vacancy', vacancy_id)
        applications = Application.objects.filter(vacancy__id=vacancy_id)
        return render(request, 'vacancy_edit.html', context={
            'form': form,
            'applications': applications,
        })
