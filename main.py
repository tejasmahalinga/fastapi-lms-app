from fastapi import FastAPI,Path,Query
from pydantic import BaseModel
from typing import Optional,List

app = FastAPI(
    title="LMS",
    description="LMS app",
    version="0.0.1",
    contact={
        "name": "Tejas",
        "email": "tj@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },)


users=[]

class User(BaseModel):
      email:str
      is_active:bool
      bio:Optional[str]


@app.get("/users",response_model=List[User])
async def get_user():
    return users


@app.post("/users")
async def post_user(user:User):
    users.append(user)
    return {"Successfully created user"}

@app.get("/users/{id}")
async def get_user(
    id:int=Path(...,description="The id of the user to retrieve",gt=2),
    q:str=Query(None,max_length=6)
    ):
    return {"user":users[id],"query":q}
