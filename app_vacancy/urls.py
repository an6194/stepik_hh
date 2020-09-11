from django.urls import path

from app_vacancy.views import VacanciesView, VacancyView, VacanciesBySpecView

urlpatterns = [
    path('', VacanciesView.as_view(), name='all_vacancies'),
    path('cat/<str:spec>/', VacanciesBySpecView.as_view(), name='vacancies_by_spec'),
    path('<int:vacancy_id>/', VacancyView.as_view(), name='vacancy'),
]
