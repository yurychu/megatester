from django.db import models
from django.conf import settings


class Cases(models.Model):
    """
    Тестовый сценарий
    """
    title = models.CharField("Заголовок тест кейса", max_length=200)
    date = models.DateTimeField("Дата создания тестового сценария")
    text = models.TextField("Текст кейса")
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "cases"
