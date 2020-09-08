from django.urls import path

from app_vacancy.views import VacancyListView, VacancyDetailView

urlpatterns = [
    path('', VacancyListView.as_view(), name='all_vacancies_view'),
    path('cat/<str:spec>/', VacancyListView.as_view(), name='vacancies_view_by_spec'),
    path('<int:vacancy_id>/', VacancyDetailView.as_view(), name='vacancy_detail_view'),
]
