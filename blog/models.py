from django.db import models

# Create your models here.




class CountView(models.Model):
    count_view = models.IntegerField(verbose_name="Количество просмотров", null=True, blank=True)

    def __str__(self):
        return f"Количество просмотров {self.count_view}"

    class Meta:
        verbose_name="Количестово просмотров"
        verbose_name_plural="Количество просмотров"