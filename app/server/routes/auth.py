### USERS API ###

import json
from fastapi import APIRouter, status, Body, HTTPException

import pydantic
from bson import ObjectId
pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str

from server.auth.jwt_handler import sign_jwt
from server.models.user import User, UserSchema, UserSignIn
from passlib.context import CryptContext


router = APIRouter(responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

hash_helper = CryptContext(schemes=["bcrypt"])

@router.get("/")
async def dashboard():
    return {
		"message": "Welcome to Auth RGX",
		"Swagger": "http://127.0.0.1:8000/docs",
		"Redocly": "http://127.0.0.1:8000/redoc"
	}

# @router.post("/register", response_model=AdminData)
@router.post("/register")
async def user_signup(user: User = Body(...)):
    user_exists = UserSchema.objects(email=user.email)
    if user_exists:
        raise HTTPException(
            status_code=409,
            detail="User with email supplied already exists"
        )

    user.password = hash_helper.encrypt(user.password)

    new_user = UserSchema(
        email=user.dict()['email'],
        lastname=user.dict()['lastname'],
        name=user.dict()['name'],
		password=user.dict()['password'],
        proyects=[]
	).save()
    return new_user

@router.post("/login")
async def user_login(user_credentials: UserSignIn = Body(...)):
    user_exists = UserSchema.objects(email=user_credentials.username)
    if user_exists:
        password = hash_helper.verify(
            user_credentials.password, user_exists[0]['password'])
        if password:
            return sign_jwt(user_credentials.username)

        raise HTTPException(
            status_code=403,
            detail="Incorrect email or password"
        )

    raise HTTPException(
        status_code=403,
        detail="Incorrect email or password"
    )
