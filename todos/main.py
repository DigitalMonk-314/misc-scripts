from fastapi import FastAPI
from todo import todo_router

app = FastAPI(title="ToDo API with Pydantic and CRUD")

@app.get("/")
async def welcome():
    return {"message": "Welcome to ToDo API!"}

# Подключаем роутер с ToDo маршрутами
app.include_router(todo_router)





