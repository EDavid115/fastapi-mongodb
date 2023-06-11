### Proyects API ###

from fastapi import APIRouter, status
from bson import ObjectId

import pydantic
pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str

router = APIRouter(responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

proyect_list = [
    {
        '_id': ObjectId('6485f25a52740ae742de0161'),
        'title': 'Bappy',
	},
    {
        '_id': ObjectId('6485f25a52740ae742de0162'),
        'title': 'WTS',
	},
    {
        '_id': ObjectId('6485f25a52740ae742de0163'),
        'title': 'Upperhand'
	},
    {
        '_id': ObjectId('6485f25a52740ae742de0164'),
        'title': 'Enel X',
	}
]


@router.get("/")
async def proyect_root():
    return {
		"message": "Welcome to Proyects RGX",
		"Swagger": "http://127.0.0.1:8000/docs",
		"Redocly": "http://127.0.0.1:8000/redoc"
	}

@router.get("/proyects")
async def proyects():
    return proyect_list

@router.get("/proyect/{_id}")
async def proyect(_id: str):
    for proyect in proyect_list:
        if str(proyect['_id']) == _id:
            return proyect
        else:
            return {}
    