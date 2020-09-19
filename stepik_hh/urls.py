"""stepik_hh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from app_home.views import MainView, CompanyView, custom_handler404, custom_handler500, \
    MyCompanyView, MyVacanciesView, MyVacancyView, CreateCompanyView, CreateVacancyView, \
    MyResumeView, CreateResumeView, SearchView
from stepik_hh.views import MyLoginView, MySignupView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('search/', SearchView.as_view(), name='search'),
    path('companies/<int:company_id>/', CompanyView.as_view(), name='company'),
    path('vacancies/', include('app_vacancy.urls')),
    path('mycompany/', MyCompanyView.as_view(), name='my_company'),
    path('mycompany/create/', CreateCompanyView.as_view(), name='create_company'),
    path('mycompany/vacancies/', MyVacanciesView.as_view(), name='my_vacancies'),
    path('mycompany/vacancies/create/', CreateVacancyView.as_view(), name='create_vacancy'),
    path('mycompany/vacancies/<int:vacancy_id>/', MyVacancyView.as_view(), name='my_vacancy'),
    path('myresume/', MyResumeView.as_view(), name='my_resume'),
    path('myresume/create/', CreateResumeView.as_view(), name='create_resume'),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', MySignupView.as_view(), name='signup'),
]

handler404 = custom_handler404
handler500 = custom_handler500

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
