from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

class Happiness(models.Model):
    date = models.DateField(default=datetime.date.today, blank=False)
    diary = models.TextField(blank = False)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    error = models.IntegerField(
                validators=[MinValueValidator(-5), MaxValueValidator(5)]
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name="happiness",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        sign = "+"
        if self.error < 0:
            sign = ""
        return self.date.strftime("%m/%d/%Y") + " - " + str(self.rating) + " Error: " + sign + str(self.error)