from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    name: str = Field(...)
    last_name: Optional[str]
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "John",
                "last_name": "Doe",
                "email": "jdoe@x.edu.ng",
                "password": "Water resources engineering",
            }
        }