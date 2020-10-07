from django.contrib import admin

from app_home.models import Application, Resume


class ApplicationAdmin(admin.ModelAdmin):
    pass


class ResumeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Resume, ResumeAdmin)
