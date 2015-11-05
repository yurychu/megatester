from django.db import models
from django.conf import settings


class Plans(models.Model):
    """
    План тестирования
    """
    title = models.CharField("Название плана тестирования", max_length=200)
    date = models.DateTimeField("Дата создания плана")
    text = models.TextField("Текст плана")
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "plans"
