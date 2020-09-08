from datetime import datetime

import mock_data as data

from app_home.models import Company
from app_vacancy.models import Vacancy, Specialty

for specialty in data.specialties:
    Specialty.objects.create(code=specialty['code'], title=specialty['title'])

for company in data.companies:
    Company.objects.create(name=company['title'], employee_count=0)

for job in data.jobs:
    Vacancy.objects.create(title=job['title'],
                           specialty=Specialty.objects.get(code=job['cat']),
                           company=Company.objects.get(name=job['company']),
                           salary_min=job['salary_from'],
                           salary_max=job['salary_to'],
                           published_at=datetime.strptime(job['posted'], '%Y-%m-%d'),
                           description=job['desc']
                           )

# To execute from InteractiveConsole run:
# with open("insert_mock_data.py") as f:
#     code = compile(f.read(), "insert_mock_data.py", 'exec')
#     exec(code)
