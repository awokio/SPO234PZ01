from django.db import models

from anketa2.models import Professia


# Create your models here.
class Mytestik(models.Model):
    professia = models.ForeignKey(Professia, on_delete=models.PROTECT, verbose_name = "Профессия")
    title = models.TextField(max_length=50, verbose_name="Название")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_strings(self))
                for field in Mytestik._meta.fields]




