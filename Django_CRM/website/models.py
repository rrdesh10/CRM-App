from django.db import models


class Record(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zipcode = models.CharField(max_length=15)


    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name}")
    