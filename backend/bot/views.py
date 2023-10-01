from rest_framework import viewsets

from bot.models import Instructions, Ksotp, KnowledgeTestSchedules, KnowledgeTestForms, MagazineDesignExamples, Sok, \
    ApplicationForms, TechnicalStudies, Reminders, NormativeDocuments, FireSafety
from bot.serializers import InstructionsSerializer, KsotpSerializer, KnowledgeTestSchedulesSerializer, \
    KnowledgeTestFormsSerializer, MagazineDesignExamplesSerializer, SokSerializer, ApplicationFormsSerializer, \
    TechnicalStudiesSerializer, RemindersSerializer, NormativeDocumentsSerializer, FireSafetySerializer


class InstructionsViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Instructions.objects.all().order_by('-id')
    serializer_class = InstructionsSerializer
    http_method_names = ['get', 'head', 'options']


class KsotpViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Ksotp.objects.all().order_by('-id')
    serializer_class = KsotpSerializer
    http_method_names = ['get', 'head', 'options']


class KnowledgeTestSchedulesViewset(viewsets.ReadOnlyModelViewSet):
    queryset = KnowledgeTestSchedules.objects.all().order_by('-id')
    serializer_class = KnowledgeTestSchedulesSerializer
    http_method_names = ['get', 'head', 'options']


class KnowledgeTestFormsViewset(viewsets.ReadOnlyModelViewSet):
    queryset = KnowledgeTestForms.objects.all().order_by('-id')
    serializer_class = KnowledgeTestFormsSerializer
    http_method_names = ['get', 'head', 'options']


class MagazineDesignExamplesViewset(viewsets.ReadOnlyModelViewSet):
    queryset = MagazineDesignExamples.objects.all().order_by('-id')
    serializer_class = MagazineDesignExamplesSerializer
    http_method_names = ['get', 'head', 'options']


class SokViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Sok.objects.all().order_by('-id')
    serializer_class = SokSerializer
    http_method_names = ['get', 'head', 'options']


class ApplicationFormsViewset(viewsets.ReadOnlyModelViewSet):
    queryset = ApplicationForms.objects.all().order_by('-id')
    serializer_class = ApplicationFormsSerializer
    http_method_names = ['get', 'head', 'options']


class TechnicalStudiesViewset(viewsets.ReadOnlyModelViewSet):
    queryset = TechnicalStudies.objects.all().order_by('-id')
    serializer_class = TechnicalStudiesSerializer
    http_method_names = ['get', 'head', 'options']


class RemindersViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Reminders.objects.all().order_by('-id')
    serializer_class = RemindersSerializer
    http_method_names = ['get', 'head', 'options']


class NormativeDocumentsViewset(viewsets.ReadOnlyModelViewSet):
    queryset = NormativeDocuments.objects.all().order_by('-id')
    serializer_class = NormativeDocumentsSerializer
    http_method_names = ['get', 'head', 'options']


class FireSafetyViewset(viewsets.ReadOnlyModelViewSet):
    queryset = FireSafety.objects.all().order_by('-id')
    serializer_class = FireSafetySerializer
    http_method_names = ['get', 'head', 'options']
