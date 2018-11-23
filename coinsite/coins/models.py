from django.db import models

# Create your models here.


class Coin(models.Model):
    denomination = models.IntegerField()
    image_url = models.CharField(max_length=1000)


    def __str__(self):
        return str(self.denomination)