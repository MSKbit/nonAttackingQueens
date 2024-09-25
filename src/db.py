# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, MetaData, Table

# Configura la cadena de conexión
DATABASE_URL = "postgresql+psycopg://postgres:admin@db:5432/Test"
engine = create_engine(DATABASE_URL)


# Crea el motor
def createConnection():
    conn = engine.connect() 

    
    

    return conn

def getQuerySelect(tableName,columnName, value):
    metadata = MetaData()

    tableObj = Table(tableName, metadata,   
    autoload_with=engine) #Table object

    return tableObj.select().where(tableObj.columns[columnName] == value)

def getQueryInsert(tableName,**kwargs):
    metadata = MetaData()

    tableObj = Table(tableName, metadata,   
    autoload_with=engine) #Table object

    return tableObj.insert().values(**kwargs)


