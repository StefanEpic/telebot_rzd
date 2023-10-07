from rest_framework import serializers

from bot.models import (
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


class InstructionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructions
        fields = ["title", "file"]


class KsotpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ksotp
        fields = ["title", "file"]


class KnowledgeTestSchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeTestSchedules
        fields = ["title", "file"]


class KnowledgeTestFormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeTestForms
        fields = ["title", "file"]


class MagazineDesignExamplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagazineDesignExamples
        fields = ["title", "file"]


class SokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sok
        fields = ["title", "file"]


class ApplicationFormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationForms
        fields = ["title", "file"]


class TechnicalStudiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalStudies
        fields = ["title", "file"]


class RemindersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminders
        fields = ["title", "file"]


class NormativeDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormativeDocuments
        fields = ["title", "file"]


class FireSafetySerializer(serializers.ModelSerializer):
    class Meta:
        model = FireSafety
        fields = ["title", "file"]
