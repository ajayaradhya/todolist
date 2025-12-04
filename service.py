from typing import List
from fastapi import HTTPException

from model import TodoItem

todos = [
    TodoItem(id=1, name="Buy groceries", description="Milk, Bread, Eggs", completed=False),
    TodoItem(id=2, name="Read a book", completed=True),
    TodoItem(id=3, name="Go for a walk", description="Evening walk in the park", completed=False),
    TodoItem(id=4, name="Write code", completed=True)
]

def get_todos() -> List[TodoItem]:
    return todos

def get_todo_by_id(todo_id: int) -> TodoItem:
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")

def delete_todo_by_id(todo_id: int) -> TodoItem:
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            return todos.pop(index)
    raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")

def update_todo_by_id(todo_id: int, updated_todo: TodoItem) -> TodoItem:
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")

def patch_todo_by_id(todo_id: int, todo_data: dict) -> TodoItem:
    print(todo_data)
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            updated_todo = todo.model_copy(update=todo_data)
            print(updated_todo)
            todos[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")

def create_todo(new_todo: TodoItem) -> TodoItem:
    todos.append(new_todo)
    return new_todo

def delete_all_todos() -> None:
    todos.clear()

def get_completed_todos() -> List[TodoItem]:
    return [todo for todo in todos if todo.completed]

def get_incomplete_todos() -> List[TodoItem]:
    return [todo for todo in todos if not todo.completed]

def mark_todo_as_completed(todo_id: int) -> TodoItem:
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index].completed = True
            return todos[index]
    raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")

def todos_count() -> int:
    return len(todos)