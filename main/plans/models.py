from django.db import models
from django.conf import settings


class Species(models.Model):
    """
    Вид деятельности
    """
    name = models.CharField("Название вида деятельности", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "species"
        verbose_name = "Вид деятельности"
        verbose_name_plural = "Виды деятельности"


class Processes(models.Model):
    """
    Процессы
    """
    name = models.CharField("Название процесса", max_length=200)
    species = models.ForeignKey(Species, verbose_name="Вид деятельности")

    def __str__(self):
        return self.name + " (" + self.species.name + ")"

    class Meta:
        db_table = "processes"
        verbose_name = "Процесс"
        verbose_name_plural = "Процессы"


class Plans(models.Model):
    """
    План тестирования
    """
    title = models.CharField("Название плана тестирования", max_length=200)
    stand_url = models.CharField("Адрес стенда, на котором проверяем", max_length=50)
    stand_user = models.CharField("Пользователь, под которым проводится проверка", max_length=50)

    process = models.ForeignKey(Processes, verbose_name="Процесс")

    date = models.DateTimeField("Дата создания плана")
    text = models.TextField("Текст плана")

    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "plans"
        verbose_name = "Тестовые план"
        verbose_name_plural = "Тестовые планы"

