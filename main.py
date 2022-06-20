from typing import List
from fastapi import FastAPI, HTTPException
from models import User,Gender, Role
from uuid import uuid4, UUID
app = FastAPI()

db: List[User] = [
    User(id=UUID("3591e6c0-e0ec-4b0a-b3cc-4fc8827c5599"),
         first_name = 'Vipul',
        last_name = 'Kumar',
         gender = Gender.male,
         roles = [Role.admin]
         ),
    User(id=UUID("98f49325-ab9f-4fda-b185-5a24af0b426b"),
         first_name = 'Isha',
        last_name = 'Gupta',
         gender = Gender.female,
         roles = [Role.student, Role.user]
         )
]

# @app.get('/')
# async def root():
#     return {"Hello":"Mundo"}


@app.get("/api/v1/users")
async def fetch_users():
    return db;


@app.post("/api/v1/users")
async def register_user(user:User):
    db.append(user)
    return {'id': user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id:UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id :{user_id} does not exist"
    )


