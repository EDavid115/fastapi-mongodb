# FAST API PROJECT

## Installation

1. Virtual environmet

   python3.9 -m venv .venv
   . .venv/bin/activate

2. Install Requirements

   pip install -r requirements.txt

3. Run local project

   python app/main.py

## Folder Structure

├── app
│   ├── __init__.py
│   ├── main.py
|	├── config.py
│   └── server
│       ├── app.py
│       ├── database.py
│       ├── models
│       └── routes
└── requirements.txt

- app/main.py file, define an entry point for running the application
- app/config.py allows us to load environment variables from a configuration
- app/server/app.py file, define the application

## Resources
- https://github.com/wpcodevo/fastapi_mongodb
- https://github.com/mouredev/Hello-Python/tree/main/Backend/FastAPI
- https://github.com/Youngestdev/fastapi-mongo
