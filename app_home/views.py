from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Count
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from app_home.forms import CompanyForm, VacancyForm, ResumeForm
from app_home.models import Company, Application, Resume
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
        company = Company.objects.filter(owner__id=request.user.id).first()
        if not company:
            return render(request, 'company_create.html')
        form = CompanyForm(instance=company)
        return render(request, 'company_edit.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        company = Company.objects.filter(owner__id=request.user.id).first()
        if not company:
            return render(request, 'company_create.html')
        CompanyForm(request.POST, request.FILES, instance=company).save()
        messages.add_message(request, messages.SUCCESS, 'Информация о компании обновлена')
        return redirect('my_company')


class CreateCompanyView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        f = CompanyForm().save(commit=False)
        f.owner = User.objects.get(id=request.user.id)
        f.save()
        return redirect('my_company')


class MyVacanciesView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        company = Company.objects.filter(owner__id=request.user.id).first()
        if not company:
            return redirect('my_company')
        vacancies = Vacancy.objects.filter(company=company).annotate(applications_count=Count('applications'))
        return render(request, 'my_vacancies_list.html', context={
            'vacancies': vacancies,
        })


class CreateVacancyView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        company = Company.objects.filter(owner__id=request.user.id).first()
        if not company:
            return redirect('my_company')
        form = VacancyForm()
        return render(request, 'vacancy_edit.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        company = Company.objects.filter(owner__id=request.user.id).first()
        if not company:
            return redirect('my_company')
        f = VacancyForm(request.POST).save(commit=False)
        f.company = company
        f.save()
        return redirect('my_vacancies')


class MyVacancyView(LoginRequiredMixin, View):

    def get(self, request, vacancy_id, *args, **kwargs):
        company = Company.objects.filter(owner__id=request.user.id).first()
        if not company:
            return redirect('my_company')
        vacancy = get_object_or_404(Vacancy, company=company, id=vacancy_id)
        form = VacancyForm(instance=vacancy)
        applications = Application.objects.filter(vacancy__id=vacancy_id)
        return render(request, 'vacancy_edit.html', context={
            'form': form,
            'applications': applications,
        })

    def post(self, request, vacancy_id, *args, **kwargs):
        company = Company.objects.filter(owner__id=request.user.id).first()
        if not company:
            return redirect('my_company')
        try:
            vacancy = Vacancy.objects.get(company=company, id=vacancy_id)
        except Vacancy.DoesNotExist:
            return redirect('my_vacancies')
        VacancyForm(request.POST, instance=vacancy).save()
        messages.add_message(request, messages.SUCCESS, 'Вакансия обновлена')
        return redirect('my_vacancy', vacancy_id)


class MyResumeView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        resume = Resume.objects.filter(user__id=request.user.id).first()
        if not resume:
            return render(request, 'resume_create.html')
        form = ResumeForm(instance=resume)
        return render(request, 'resume_edit.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        resume = Resume.objects.filter(user__id=request.user.id).first()
        if not resume:
            return render(request, 'resume_create.html')
        ResumeForm(request.POST, instance=resume).save()
        messages.add_message(request, messages.SUCCESS, 'Ваше резюме обновлено!')
        return redirect('my_resume')


class CreateResumeView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(request, 'resume_edit.html', context={
            'form': ResumeForm(),
        })

    def post(self, request, *args, **kwargs):
        f = ResumeForm(request.POST).save(commit=False)
        f.user = User.objects.get(id=request.user.id)
        f.save()
        messages.add_message(request, messages.SUCCESS, 'Ваше резюме успешно создано!')
        return redirect('my_resume')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Похоже Вы заблудились...')


def custom_handler500(request):
    return HttpResponseServerError('Надо мастера звать - пусть чинит.')
