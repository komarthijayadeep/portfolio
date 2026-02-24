from django.contrib import admin
from .models import Project, Certificate

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'date_issued', 'created_date')
    list_filter = ('issuer', 'date_issued')
    search_fields = ('title', 'issuer', 'description')
