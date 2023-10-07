import os

from django.db import models
from pytils.translit import slugify


class Instructions(models.Model):
    class Meta:
        verbose_name = "Инструкцию"
        verbose_name_plural = "Инструкции"

    def get_slug_name(self, filename: str) -> str:
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        path = "".join(["instructions/", new_filename])
        return path

    def __str__(self) -> models.CharField:
        return self.title

    title = models.CharField(max_length=40, unique=True, verbose_name="Название")
    file = models.FileField(upload_to=get_slug_name, max_length=40, verbose_name="Инструкция")


class Ksotp(models.Model):
    class Meta:
        verbose_name = "КСОТ-П"
        verbose_name_plural = "КСОТ-П"

    def get_slug_name(self, filename: str) -> str:
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        path = "".join(["ksot_p/", new_filename])
        return path

    def __str__(self) -> models.CharField:
        return self.title

    title = models.CharField(max_length=40, unique=True, verbose_name="Название")
    file = models.FileField(upload_to=get_slug_name, max_length=40, verbose_name="КСОТ-П")


class KnowledgeTestSchedules(models.Model):
    class Meta:
        verbose_name = "График проверки знаний"
        verbose_name_plural = "Графики проверки знаний"

    def get_slug_name(self, filename: str) -> str:
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        path = "".join(["knowledge_test_schedules/", new_filename])
        return path

    def __str__(self) -> models.CharField:
        return self.title

    title = models.CharField(max_length=40, unique=True, verbose_name="Название")
    file = models.FileField(
        upload_to=get_slug_name,
        max_length=40,
        verbose_name="График проверки знаний",
    )


class KnowledgeTestForms(models.Model):
    class Meta:
        verbose_name = "Билет для проверки знаний"
        verbose_name_plural = "Билеты для проверки знаний"

    def get_slug_name(self, filename: str) -> str:
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        path = "".join(["knowledge_test_forms/", new_filename])
        return path

    def __str__(self) -> models.CharField:
        return self.title

    title = models.CharField(max_length=40, unique=True, verbose_name="Название")
    file = models.FileField(
        upload_to=get_slug_name,
        max_length=40,
        verbose_name="Билет для проверки знаний",
    )


class MagazineDesignExamples(models.Model):
    class Meta:
        verbose_name = "Пример оформления журналов"
        verbose_name_plural = "Примеры оформления журналов"

    def get_slug_name(self, filename: str) -> str:
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        path = "".join(["magazine_design_examples/", new_filename])
        return path

    def __str__(self) -> models.CharField:
        return self.title

    title = models.CharField(max_length=40, unique=True, verbose_name="Название")
    file = models.FileField(
        upload_to=get_slug_name,
        max_length=40,
        verbose_name="Пример оформления журналов",
    )


class Sok(models.Model):
    class Meta:
        verbose_name = "СОК"
        verbose_name_plural = "СОК"

    def get_slug_name(self, filename: str) -> str:
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        path = "".join(["sok/", new_filename])
        return path

    def __str__(self) -> models.CharField:
        return self.title

    title = models.CharField(max_length=40, unique=True, verbose_name="Название")
    file = models.FileField(upload_to=get_slug_name, max_length=40, verbose_name="СОК")


class ApplicationForms(models.Model):
    class Meta:
        verbose_name = "Бланк заявлений"
        verbose_name_plural = "Бланки заявлений"

    def get_slug_name(self, filename: str) -> str:
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        path = "".join(["application_forms/", new_filename])
        return path

    def __str__(self) -> models.CharField:
        return self.title

    title = models.CharField(max_length=40, unique=True, verbose_name="Название")
    file = models.FileField(upload_to=get_slug_name, max_length=40, verbose_name="Бланк заявлений")


class TechnicalStudies(models.Model):
    class Meta:
        verbose_name = "Техническую учебу"
        verbose_name_plural = "Техническая учеба"

    def get_slug_name(self, filename: str) -> str:
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        path = "".join(["technical_studies/", new_filename])
        return path

    def __str__(self) -> models.CharField:
        return self.title

    title = models.CharField(max_length=40, unique=True, verbose_name="Название")
    file = models.FileField(upload_to=get_slug_name, max_length=40, verbose_name="Техническая учеба")


class Reminders(models.Model):
    class Meta:
        verbose_name = "Памятку"
        verbose_name_plural = "Памятки"

    def get_slug_name(self, filename: str) -> str:
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        path = "".join(["reminders/", new_filename])
        return path

    def __str__(self) -> models.CharField:
        return self.title

    title = models.CharField(max_length=40, unique=True, verbose_name="Название")
    file = models.FileField(upload_to=get_slug_name, max_length=40, verbose_name="Памятка")


class NormativeDocuments(models.Model):
    class Meta:
        verbose_name = "Нормативную документацию"
        verbose_name_plural = "Нормативная документация"

    def get_slug_name(self, filename: str) -> str:
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        path = "".join(["normative_documents/", new_filename])
        return path

    def __str__(self) -> models.CharField:
        return self.title

    title = models.CharField(max_length=40, unique=True, verbose_name="Название")
    file = models.FileField(
        upload_to=get_slug_name,
        max_length=40,
        verbose_name="Нормативная документация",
    )


class FireSafety(models.Model):
    class Meta:
        verbose_name = "Пожарную безопасность"
        verbose_name_plural = "Пожарная безопасность"

    def get_slug_name(self, filename: str) -> str:
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        path = "".join(["fire_safety/", new_filename])
        return path

    def __str__(self) -> models.CharField:
        return self.title

    title = models.CharField(max_length=40, unique=True, verbose_name="Название")
    file = models.FileField(
        upload_to=get_slug_name,
        max_length=40,
        verbose_name="Пожарная безопасность",
    )
