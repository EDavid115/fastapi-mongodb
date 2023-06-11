### USERS API ###

import json
from fastapi import APIRouter, status, Request

import pydantic
from bson import ObjectId
pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str

from server.auth.jwt_handler import decode_jwt
from server.models.user import UserSchema
from passlib.context import CryptContext


router = APIRouter(responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

hash_helper = CryptContext(schemes=["bcrypt"])

@router.get("/")
async def dashboard():
    return {
		"message": "Welcome to Users RGX",
		"Swagger": "http://127.0.0.1:8000/docs",
		"Redocly": "http://127.0.0.1:8000/redoc"
	}

@router.post("/list")
async def users_list():
    user_list = UserSchema.objects()
    return json.loads(user_list.to_json())

@router.post("/me")
async def users_list(request: Request):
    token = request.headers.get('authorization').split(' ')[1]
    token_data = decode_jwt(token)
    user_list = UserSchema.objects.get(email=token_data['user_id'])
    return json.loads(user_list.to_json())