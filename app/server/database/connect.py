from mongoengine import connect, disconnect

def connectDB(host, db_name):
    connect(db_name, host=host, alias='RGX')
    return 'RGX'

def disconnectDB(db):
    disconnect(alias=db)