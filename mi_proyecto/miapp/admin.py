from django.contrib import admin
from .models import Patient, Diagnosis


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'dni', 'birth_date',
        'gender', 'phone', 'email', 'blood_type', 'created_at'
    )
    search_fields = ('first_name', 'last_name', 'dni', 'email', 'phone')
    list_filter = ('gender', 'blood_type', 'created_at')
    ordering = ('last_name', 'first_name')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Datos personales', {
            'fields': ('first_name', 'last_name', 'dni', 'birth_date', 'gender')
        }),
        ('Contacto', {
            'fields': ('phone', 'email', 'address')
        }),
        ('Información médica', {
            'fields': ('blood_type',)
        }),
        ('Sistema', {
            'fields': ('created_at',)
        }),
    )


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = (
        'patient', 'date', 'icd_code', 'short_description', 'is_active'
    )
    list_filter = ('is_active', 'date')
    search_fields = ('patient__first_name', 'patient__last_name', 'icd_code', 'description')
    ordering = ('-date',)
    autocomplete_fields = ('patient',)
    readonly_fields = ('date',)

    def short_description(self, obj):
        return (obj.description[:50] + '...') if len(obj.description) > 50 else obj.description
    short_description.short_description = 'Descripción'
