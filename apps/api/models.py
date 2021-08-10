from django.db import models


class Log(models.Model):
    number = models.IntegerField(default=0)
    date = models.DateTimeField('print date')

    def __str__(self):
        return "Number: " + str(self.number) + "  Date: " + str(self.date)
