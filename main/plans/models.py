from django.db import models
from django.conf import settings


class Plans(models.Model):
    """
    План тестирования
    """
    title = models.CharField("Название плана тестирования", max_length=200)
    stand_url = models.CharField("Адрес стенда, на котором проверяем", max_length=50)
    stand_user = models.CharField("Пользователь, под которым проводится проверка", max_length=50)

    species = models.ForeignKey(Species)

    date = models.DateTimeField("Дата создания плана")
    text = models.TextField("Текст плана")

    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "plans"


class Species(models.Model):
    """
    Вид деятельности
    """
    name = models.CharField("Название вида деятельности", max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "species"


class Processes(models.Model):
    """
    Процессы
    """
    name = models.CharField("Название процесса", max_length=200)
    species = models.ForeignKey(Species)

    class Meta:
        db_table = "processes"

