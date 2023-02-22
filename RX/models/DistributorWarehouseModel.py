from RX.models.GeneralModel import Entity
from django.db import models


class DistributorWarehouse(Entity):
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    License = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.Name} | {self.Address}'
