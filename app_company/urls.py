from django.urls import path

from app_company.views import MyCompanyView, MyVacanciesView, MyVacancyView, CreateCompanyView, CreateVacancyView

urlpatterns = [
    path('', MyCompanyView.as_view(), name='my_company'),
    path('create/', CreateCompanyView.as_view(), name='create_company'),
    path('vacancies/', MyVacanciesView.as_view(), name='my_vacancies'),
    path('vacancies/create/', CreateVacancyView.as_view(), name='create_vacancy'),
    path('vacancies/<int:vacancy_id>/', MyVacancyView.as_view(), name='my_vacancy'),
]
