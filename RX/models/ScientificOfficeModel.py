import uuid

from django.conf import settings
from django.db import models
# from RX.models.DistributorWarehouseModel import DistributorWarehouse

# Create your models here.
from RX.models.GeneralModel import Entity, Manufactures


class ScientificOffice(Entity):
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    License = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.Name}'


class ScientificOfficeItems(Entity):
    ProductName = models.CharField(max_length=100)
    ChemicalName = models.CharField(max_length=100)
    Dosage = models.CharField(max_length=50)
    Package = models.CharField(max_length=50)
    ProductDate = models.DateField()
    ExpireDate = models.DateField()
    BatchNumber = models.CharField(max_length=50)
    ManufactureID = models.ForeignKey(Manufactures, on_delete=models.PROTECT)
    ScientificOfficeID = models.ForeignKey(ScientificOffice, on_delete=models.PROTECT)

    def __str__(self):
        return f'Product: {self.ProductName} || SB: {self.ScientificOfficeID}'


class ScientificOfficeStock(Entity):
    ItemID = models.ForeignKey(ScientificOfficeItems, on_delete=models.PROTECT)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    ProductDate = models.DateField()
    ExpireDate = models.DateField()
    Quantity = models.IntegerField()

    def __str__(self):
        return f'{self.ItemID} || Price {self.Price}'


class DistributorWarehouse(Entity):
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    License = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.Name} | {self.Address}'


class Invoices(Entity):
    InvoiceNumber = models.IntegerField()
    InvoiceDate = models.DateTimeField(auto_now_add=True, editable=False)
    InvoiceDW = models.ForeignKey(DistributorWarehouse, on_delete=models.DO_NOTHING, null=True)
    PaymentTerms = models.PositiveIntegerField(default=0)
    ContactDetails = models.CharField(max_length=100, blank=True, null=True)
    DueDate = models.DateField()
    ProductName = models.ForeignKey(ScientificOfficeStock, on_delete=models.DO_NOTHING)
    Quantitiy = models.PositiveIntegerField()
    SellPrice = models.DecimalField(decimal_places=2, max_digits=10)

    # Note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.InvoiceNumber} || {self.InvoiceDW} '
