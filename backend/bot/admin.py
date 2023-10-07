from django.contrib import admin
from .models import (
    Instructions,
    Ksotp,
    KnowledgeTestSchedules,
    KnowledgeTestForms,
    MagazineDesignExamples,
    Sok,
    ApplicationForms,
    TechnicalStudies,
    Reminders,
    NormativeDocuments,
    FireSafety,
)

admin.site.register(Instructions)
admin.site.register(Ksotp)
admin.site.register(KnowledgeTestSchedules)
admin.site.register(KnowledgeTestForms)
admin.site.register(MagazineDesignExamples)
admin.site.register(Sok)
admin.site.register(ApplicationForms)
admin.site.register(TechnicalStudies)
admin.site.register(Reminders)
admin.site.register(NormativeDocuments)
admin.site.register(FireSafety)
