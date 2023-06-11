### DASHBOARD API ###

from fastapi import APIRouter, status
from bson import ObjectId

import pydantic
pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str

router = APIRouter(responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

metrics_list = [
    {
        '_id': ObjectId('6485f25a52740ae742de0161'),
        'title': 'Traffic',
        'type': 'traffic',
        'amount': 350897,
        'percentage': 3.48
	},
    {
        '_id': ObjectId('6485f25a52740ae742de0162'),
        'title': 'New Users',
        'type': 'users',
        'amount': 2356,
        'percentage': -3.8
	},
    {
        '_id': ObjectId('6485f25a52740ae742de0163'),
        'title': 'Sales',
        'type': 'sales',
        'amount': 924,
        'percentage': -1.10
	},
    {
        '_id': ObjectId('6485f25a52740ae742de0164'),
        'title': 'Performance',
        'type': 'performance',
        'amount': 49.56,
        'percentage': 12
	}
]


@router.get("/")
async def dashboard():
    return {
		"message": "Welcome to Dashboard RGX",
		"Swagger": "http://127.0.0.1:8000/docs",
		"Redocly": "http://127.0.0.1:8000/redoc"
	}

@router.get("/metrics")
async def metrics():
    return metrics_list

@router.get("/metric/{_id}")
async def metric(_id: str):
    for metric in metrics_list:
        if str(metric['_id']) == _id:
            return metric
        else:
            return {}