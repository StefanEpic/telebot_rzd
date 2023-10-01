from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from django.urls import path, include

from bot.views import InstructionsViewset, KsotpViewset, KnowledgeTestSchedulesViewset, KnowledgeTestFormsViewset, \
    MagazineDesignExamplesViewset, SokViewset, ApplicationFormsViewset, TechnicalStudiesViewset, RemindersViewset, \
    NormativeDocumentsViewset, FireSafetyViewset

router = routers.DefaultRouter()
router.register(r'instructions', InstructionsViewset, basename='instructions')
router.register(r'ksot_p', KsotpViewset, basename='ksot_p')
router.register(r'knowledge_test_schedules', KnowledgeTestSchedulesViewset, basename='knowledge_test_schedules')
router.register(r'knowledge_test_forms', KnowledgeTestFormsViewset, basename='knowledge_test_forms')
router.register(r'magazine_design_examples', MagazineDesignExamplesViewset, basename='magazine_design_examples')
router.register(r'sok', SokViewset, basename='sok')
router.register(r'application_forms', ApplicationFormsViewset, basename='application_forms')
router.register(r'technical_studies', TechnicalStudiesViewset, basename='technical_studies')
router.register(r'reminders', RemindersViewset, basename='reminders')
router.register(r'normative_documents', NormativeDocumentsViewset, basename='normative_documents')
router.register(r'fire_safety', FireSafetyViewset, basename='fire_safety')

urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
