from typing import Optional
from pydantic import BaseModel, EmailStr, Field

import datetime
from mongoengine.document import DynamicDocument
from mongoengine.fields import BooleanField, DateTimeField, EmailField, ListField, StringField
from fastapi.security import HTTPBasicCredentials


class UserSchema(DynamicDocument):
    email = EmailField(required=True)
    name = StringField(required=True)
    lastname = StringField(required=True)
    password = StringField(required=True)
    proyects = ListField(StringField(), required=False)
    createdAt = DateTimeField(default=datetime.datetime.now)
    updatedAt = DateTimeField(default=datetime.datetime.now)
    deleted = BooleanField(default=False)

    meta = {
        'collection': 'users',
        'db_alias': 'RGX'
    }


class User(BaseModel):
    email: EmailStr = Field(...)
    name: str = Field(...)
    lastname: Optional[str]
    password: str = Field(...)
    proyects: Optional[list]

    class Config:
        schema_extra = {
            "example": {
                "name": "John",
                "lastname": "Doe",
                "email": "jdoe@x.edu.ng",
                "password": "Water resources engineering",
                "proyects": ['Bappy']
            }
        }


class UserSignIn(HTTPBasicCredentials):
    class Config:
        schema_extra = {
            "example": {
                "username": "jdoe@x.edu.ng",
                "password": "Water resources engineering"
            }
        }