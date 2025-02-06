from sqlalchemy import String, Table, Column,Integer
from config.db import meta

users = Table(
    'user',meta,
    Column('id',Integer,primary_key=True),
    Column('name', String(255)),
    Column('email',String(255)),
    Column('password',String(255)),
)