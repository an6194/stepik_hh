from django.http import Http404, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views import View

from app_home.models import Company
from app_vacancy.models import Specialty, Vacancy


class MainView(View):

    def get(self, request, *args, **kwargs):
        specs = Specialty.objects.all()
        companies = Company.objects.all()
        return render(request, 'index.html', context={
            'specs': specs,
            'companies': companies,
        })


class CompanyView(View):

    def get(self, request, company_id, *args, **kwargs):
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            raise Http404
        vacancies = Vacancy.objects.filter(company=company)
        return render(request, 'company.html', context={
            'company': company,
            'vacancies': vacancies,
        })


def custom_handler404(request, exception):
    return HttpResponseNotFound('Похоже Вы заблудились...')


def custom_handler500(request):
    return HttpResponseServerError('Надо мастера звать - пусть чинит.')
