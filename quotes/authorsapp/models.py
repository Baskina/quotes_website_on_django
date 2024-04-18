from django.db import models


class Author(models.Model):
    fullname = models.CharField(max_length=50, null=False)
    born_date = models.DateField()
    born_location = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.fullname}"
