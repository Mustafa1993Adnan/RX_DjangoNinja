from RX.models import ScientificOffice
from RX.models.GeneralModel import Entity, Manufactures
from django.db import models


# class DWItems(Entity):
#     ProductName = models.CharField(max_length=100)
#     ChemicalName = models.CharField(max_length=100)
#     Dosage = models.CharField(max_length=50)
#     Package = models.CharField(max_length=50)
#     ProductDate = models.DateField()
#     ExpireDate = models.DateField()
#     BatchNumber = models.CharField(max_length=50)
#     ManufactureID = models.ForeignKey(Manufactures, on_delete=models.PROTECT)
#     ScientificOfficeID = models.ForeignKey(ScientificOffice, on_delete=models.PROTECT)
