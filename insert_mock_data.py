from datetime import datetime
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stepik_hh.settings')
django.setup()


import mock_data as data

from app_home.models import Company
from app_vacancy.models import Vacancy, Specialty


if __name__ == '__main__':

    Specialty.objects.bulk_create(
        [
            Specialty(code=specialty['code'], title=specialty['title'])
            for specialty in data.specialties
        ]
    )

    Company.objects.bulk_create(
        [
            Company(name=company['title'], employee_count=0)
            for company in data.companies
        ]
    )

    Vacancy.objects.bulk_create(
        [
            Vacancy(
                title=job['title'],
                specialty=Specialty.objects.get(code=job['cat']),
                company=Company.objects.get(name=job['company']),
                salary_min=job['salary_from'],
                salary_max=job['salary_to'],
                published_at=datetime.strptime(job['posted'], '%Y-%m-%d'),
                description=job['desc'],
            )
            for job in data.jobs
        ]
    )
