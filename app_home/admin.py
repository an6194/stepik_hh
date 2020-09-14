from django.contrib import admin

from app_home.models import Company, Application


class CompanyAdmin(admin.ModelAdmin):
    pass


class ApplicationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company, CompanyAdmin)
admin.site.register(Application, ApplicationAdmin)
