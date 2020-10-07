from django.contrib import admin

from app_company.models import Company


class CompanyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company, CompanyAdmin)
