from fastapi import FastAPI, status, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models
from app.db import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return "todooo"

@app.post("/todo", status_code=status.HTTP_201_CREATED)
def create_todo():
    return "create todo item"

@app.get("/todo/{id}")
def read_todo(id: int):
    return "read todo item with id "+ str(id)

@app.put("/todo/{id}")
def update_todo(id: int):
    return "update todo item with id "+ str(id)

@app.delete("/todo/{id}")
def delete_todo(id: int):
    return "delete todo item with id "+ str(id)

@app.get("/todo")
def read_todo_list():
    return "read todo list"