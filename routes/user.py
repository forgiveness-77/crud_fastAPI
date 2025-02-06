from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User

user = APIRouter()

@user.get("/")
async def read_data():
    result = conn.execute(users.select()).fetchall()
    return [{"id": row.id, "name": row.name, "email": row.email, "password": row.password} for row in result]


@user.get("/{id}")
async def read_data(id: int):
    result = conn.execute(users.select().where(users.c.id == id)).fetchall()
    return [{"id": row.id, "name": row.name, "email": row.email, "password": row.password} for row in result]


@user.post("/")
async def write_data(user: User):
    # Insert the new user data
    conn.execute(users.insert().values(
        name=user.name,
        email=user.email,
        password=user.password,
    ))

    conn.commit()  # Ensure the changes are committed

    result = conn.execute(users.select()).fetchall()
    return [{"id": row.id, "name": row.name, "email": row.email, "password": row.password} for row in result]


@user.put("/{id}")
async def update_data(id: int, user: User):
    conn.execute(users.update()
                 .where(users.c.id == id)
                 .values(name=user.name, email=user.email, password=user.password))
    result = conn.execute(users.select()).fetchall()
    return [{"id": row.id, "name": row.name, "email": row.email, "password": row.password} for row in result]


@user.delete("/{id}")
async def delete_data(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    result = conn.execute(users.select()).fetchall()
    return [{"id": row.id, "name": row.name, "email": row.email, "password": row.password} for row in result]