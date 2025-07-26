from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel, Field

app = FastAPI()

todo_lists =[
    {"id": 1, "name": "Groceries"},
    {"id": 2, "name": "Work Tasks"},
    {"id": 3, "name": "Personal Projects"},
    {"id": 4, "name": "Fitness Goals"}
]



@app.get("/")
def index():
    return {"Hello": "World"}


@app.post("/api/v1/moods")
def create_mood(mood: dict):
    return {"mood": mood}

@app.get("/api/v1/moods")
def get_moods():
    return {"moods": ["happy", "sad", "angry", "excited"]}

# @app.get("/todos/{todo_id}") #using path parameter
# def get_todo(todo_id: int, q: Union[str, None] = None):
#     for todo in todo_lists:
#         if todo["id"] == todo_id:
#             return {"todo": todo, "query": q}
#     return {"error": "Todo not found"}, 404

# @app.get("/todos")
# def get_all_todos(first_n: int = None): #using query parameter
#     if first_n is not None:
#         return {"todos": todo_lists[:first_n]} 
#     return {"todos": todo_lists}

# @api.post("/todos")
# def create_todo(todo: dict):
#     new_id = max(todo["id"] for todo in todo_lists) + 1 if todo_lists else 1
#     todo["id"] = new_id
#     todo_lists.append(todo)
#     return {"todo": todo}
