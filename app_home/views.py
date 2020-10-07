from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Count, Q
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from app_company.models import Company
from app_home.forms import ResumeForm
from app_home.models import Resume
from app_vacancy.models import Specialty, Vacancy


class MainView(View):

    def get(self, request, *args, **kwargs):
        specs = Specialty.objects.all().annotate(vacancies_count=Count('vacancies'))
        companies = Company.objects.all().annotate(vacancies_count=Count('vacancies'))
        return render(request, 'index.html', context={
            'specs': specs,
            'companies': companies,
        })


class SearchView(View):

    def get(self, request, *args, **kwargs):
        query = request.GET['s']
        vacancies = Vacancy.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return render(request, 'search.html', context={
            'vacancies': vacancies,
        })


class CompanyView(View):

    def get(self, request, company_id, *args, **kwargs):
        company = get_object_or_404(Company, id=company_id)
        vacancies = Vacancy.objects.filter(company=company)
        return render(request, 'company.html', context={
            'company': company,
            'vacancies': vacancies,
        })


class MyResumeView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        try:
            resume = request.user.resume
        except Resume.DoesNotExist:
            return render(request, 'resume_create.html')
        form = ResumeForm(instance=resume)
        return render(request, 'resume_edit.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        try:
            resume = request.user.resume
        except Resume.DoesNotExist:
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
