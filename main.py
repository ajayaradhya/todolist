from fastapi import FastAPI

from model import TodoItem
import service as service

app = FastAPI()

@app.get("/todos/", response_model=list[TodoItem])
def read_root():
    return service.get_todos()

@app.get("/todos/{todo_id}", response_model=TodoItem)
def get_todo(todo_id: int):
    return service.get_todo_by_id(todo_id)

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    return service.delete_todo_by_id(todo_id)

@app.post("/todos/", response_model=TodoItem)
def create_todo_item(todo: TodoItem):
    return service.create_todo(todo)

@app.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo_item(todo_id: int, todo: TodoItem):
    return service.update_todo_by_id(todo_id, todo)

@app.patch("/todos/{todo_id}", response_model=TodoItem)
def patch_todo_item(todo_id: int, todo_data: dict):
    return service.patch_todo_by_id(todo_id, todo_data)

@app.delete("/todos/")
def delete_all_todo_items():
    service.delete_all_todos()
    return {"detail": "All todos deleted"}

@app.get("/todos/completed/", response_model=list[TodoItem])
def get_completed_todo_items():
    return service.get_completed_todos()

@app.get("/todos/incomplete/", response_model=list[TodoItem])
def get_incomplete_todo_items():
    return service.get_incomplete_todos()   

@app.post("/todos/{todo_id}/complete", response_model=TodoItem)
def mark_todo_completed(todo_id: int):  
    return service.mark_todo_as_completed(todo_id)