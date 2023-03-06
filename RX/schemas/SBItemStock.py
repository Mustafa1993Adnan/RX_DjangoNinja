import datetime

from ninja import Schema
from pydantic.types import UUID4

from RX.models import ScientificOfficeStock
from RX.schemas.DWSchema import DWOut


class ManufacturesOut(Schema):
    ManufactureName: str
    Country: str


class ScientificOfficeOut(Schema):
    id: UUID4
    Name: str
    Address: str
    Description: str
    License: str


class ItemsOut(Schema):
    id: UUID4
    ProductName: str
    Dosage: str
    ManufactureID: ManufacturesOut
    ScientificOfficeID: ScientificOfficeOut


class SBStockOut(Schema):
    ItemID: ItemsOut
    id: UUID4
    Price: str
    ProductDate: datetime.date
    ExpireDate: datetime.date
    Quantity: int


class SBInvoiceInBody(Schema):
    InvoiceNumber: int
    invoice_date: datetime.date
    InvoiceDW: UUID4
    PaymentTerms: int
    DueDate: datetime.date
    ProductName: UUID4
    Quantitiy: int
    SellPrice: float


class SBInvoiceOut(Schema):
    id: UUID4
    InvoiceNumber: int
    InvoiceDate: datetime.datetime = None
    InvoiceDW: DWOut
    PaymentTerms: int
    DueDate: datetime.date
    ProductName: SBStockOut = None
    Quantitiy: int
    SellPrice: float
