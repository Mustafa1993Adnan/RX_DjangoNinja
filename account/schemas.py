import datetime
from uuid import UUID

from ninja import Schema
from ninja import Field
from pydantic import EmailStr

from account.models import User


class PasswordSchema(Schema):
    password1: str = Field(min_length=6)
    password2: str = Field(min_length=6)


class AccountCreateBody(PasswordSchema):
    name: str = Field(min_length=4)
    email: EmailStr


class AccountLoginBody(Schema):
    email: EmailStr
    password: str = Field(min_length=6)


class UserTypeOut(Schema):
    type: str


class UserOut(Schema):
    id: UUID
    name: str
    email: str
    gender: str
    userType: UserTypeOut
    phone: str
    birth_date: datetime.date = None


class AccountOut(Schema):
    token: str
    user: UserOut


class PasswordResetToken(Schema):
    token: str


class OtpIn(Schema):
    otp: int = Field(..., ge=1000, le=9999)


class AccountInfo(Schema):
    name: str
    email: EmailStr
    profile: str = None
    gender: str = None
    phone: str = None
    birth_date: datetime.date = None


class AccountUpdate(Schema):
    name: str = None
    gender: str = None
    phone: str = None
    birth_date: datetime.date = None
