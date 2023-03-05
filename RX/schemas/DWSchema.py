from ninja import Schema
from pydantic.types import UUID4


class DWOut(Schema):
    id: UUID4
    Name: str
    Address: str
    Description: str
    License: str
