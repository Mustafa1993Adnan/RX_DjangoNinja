import datetime

from ninja import Schema
from pydantic.types import UUID4


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
