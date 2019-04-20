from django.db import models


class ActiveUser(models.Model):
    count = models.DecimalField(max_digits=19, decimal_places=3)
    time = models.DateTimeField()
    def __str__(self):
        return (f"{self.time}, {self.count}")
