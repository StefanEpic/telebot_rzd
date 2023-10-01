import os

from django.db import models
from pytils.translit import slugify


class Instructions(models.Model):
    class Meta:
        verbose_name = u'Инструкцию'
        verbose_name_plural = u'Инструкции'

    def get_slug_name(self, filename):
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        path = ''.join(['instructions/', new_filename])
        return path

    def __str__(self):
        return self.title

    title = models.CharField(max_length=40, unique=True, verbose_name='Название')
    file = models.FileField(upload_to=get_slug_name, max_length=40, verbose_name='Инструкция')


class Ksotp(models.Model):
    class Meta:
        verbose_name = u'КСОТ-П'
        verbose_name_plural = u'КСОТ-П'

    def get_slug_name(self, filename):
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        path = ''.join(['ksot_p/', new_filename])
        return path

    def __str__(self):
        return self.title

    title = models.CharField(max_length=40, unique=True, verbose_name='Название')
    file = models.FileField(upload_to=get_slug_name, max_length=40, verbose_name='КСОТ-П')


class KnowledgeTestSchedules(models.Model):
    class Meta:
        verbose_name = u'График проверки знаний'
        verbose_name_plural = u'Графики проверки знаний'

    def get_slug_name(self, filename):
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        path = ''.join(['knowledge_test_schedules/', new_filename])
        return path

    def __str__(self):
        return self.title

    title = models.CharField(max_length=40, unique=True, verbose_name='Название')
    file = models.FileField(upload_to=get_slug_name, max_length=40, verbose_name='График проверки знаний')


class KnowledgeTestForms(models.Model):
    class Meta:
        verbose_name = u'Билет для проверки знаний'
        verbose_name_plural = u'Билеты для проверки знаний'

    def get_slug_name(self, filename):
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        path = ''.join(['knowledge_test_forms/', new_filename])
        return path

    def __str__(self):
        return self.title

    title = models.CharField(max_length=40, unique=True, verbose_name='Название')
    file = models.FileField(upload_to=get_slug_name, max_length=40, verbose_name='Билет для проверки знаний')


class MagazineDesignExamples(models.Model):
    class Meta:
        verbose_name = u'Пример оформления журналов'
        verbose_name_plural = u'Примеры оформления журналов'

    def get_slug_name(self, filename):
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        path = ''.join(['magazine_design_examples/', new_filename])
        return path

    def __str__(self):
        return self.title

    title = models.CharField(max_length=40, unique=True, verbose_name='Название')
    file = models.FileField(upload_to=get_slug_name, max_length=40, verbose_name='Пример оформления журналов')


class Sok(models.Model):
    class Meta:
        verbose_name = u'СОК'
        verbose_name_plural = u'СОК'

    def get_slug_name(self, filename):
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        path = ''.join(['sok/', new_filename])
        return path

    def __str__(self):
        return self.title

    title = models.CharField(max_length=40, unique=True, verbose_name='Название')
    file = models.FileField(upload_to=get_slug_name, max_length=40, verbose_name='СОК')


class ApplicationForms(models.Model):
    class Meta:
        verbose_name = u'Бланк заявлений'
        verbose_name_plural = u'Бланки заявлений'

    def get_slug_name(self, filename):
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        path = ''.join(['application_forms/', new_filename])
        return path

    def __str__(self):
        return self.title

    title = models.CharField(max_length=40, unique=True, verbose_name='Название')
    file = models.FileField(upload_to=get_slug_name, max_length=40, verbose_name='Бланк заявлений')


class TechnicalStudies(models.Model):
    class Meta:
        verbose_name = u'Техническую учебу'
        verbose_name_plural = u'Техническая учеба'

    def get_slug_name(self, filename):
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        path = ''.join(['technical_studies/', new_filename])
        return path

    def __str__(self):
        return self.title

    title = models.CharField(max_length=40, unique=True, verbose_name='Название')
    file = models.FileField(upload_to=get_slug_name, max_length=40, verbose_name='Техническая учеба')


class Reminders(models.Model):
    class Meta:
        verbose_name = u'Памятку'
        verbose_name_plural = u'Памятки'

    def get_slug_name(self, filename):
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        path = ''.join(['reminders/', new_filename])
        return path

    def __str__(self):
        return self.title

    title = models.CharField(max_length=40, unique=True, verbose_name='Название')
    file = models.FileField(upload_to=get_slug_name, max_length=40, verbose_name='Памятка')


class NormativeDocuments(models.Model):
    class Meta:
        verbose_name = u'Нормативную документацию'
        verbose_name_plural = u'Нормативная документация'

    def get_slug_name(self, filename):
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        path = ''.join(['normative_documents/', new_filename])
        return path

    def __str__(self):
        return self.title

    title = models.CharField(max_length=40, unique=True, verbose_name='Название')
    file = models.FileField(upload_to=get_slug_name, max_length=40, verbose_name='Нормативная документация')


class FireSafety(models.Model):
    class Meta:
        verbose_name = u'Пожарную безопасность'
        verbose_name_plural = u'Пожарная безопасность'

    def get_slug_name(self, filename):
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        path = ''.join(['fire_safety/', new_filename])
        return path

    def __str__(self):
        return self.title

    title = models.CharField(max_length=40, unique=True, verbose_name='Название')
    file = models.FileField(upload_to=get_slug_name, max_length=40, verbose_name='Пожарная безопасность')
