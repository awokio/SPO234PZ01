from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Professia(models.Model):
    title = models.TextField(max_length=50, verbose_name="Профессия")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_strings(self))
                for field in Professia._meta.fields]




class Gragdanin(User):
    mydata = models.TextField(max_length=50, verbose_name="Название")
    #мы умные 100 працентава ми здали рускя язика на сти баллив!!!!!!!!!!!!!!!!111!!!!!!! и пастипили в маскаву сталица расися