from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate
from app.database import get_db
from app.utils.auth import get_current_user

router = APIRouter()

@router.post("/tasks")
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    new_task = Task(**task.dict(), user_id=current_user.id)
    db.add(new_task)
    db.commit()
    return new_task

@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    return db.query(Task).filter(Task.user_id == current_user.id).all()

@router.patch("/tasks/{id}")
def update_task(id: int, task: TaskUpdate, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    db_task = db.query(Task).filter(Task.id == id, Task.user_id == current_user.id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db_task.completed = task.completed
    db.commit()
    return db_task

@router.delete("/tasks/completed")
async def delete_completed_tasks(db: Session = Depends(get_db)):
    completed_tasks = db.query(Task).filter(Task.completed == True).all()

    if not completed_tasks:
        raise HTTPException(status_code=404, detail="No completed tasks found")

    db.query(Task).filter(Task.completed == True).delete()
    db.commit()
    return {"msg": f"{len(completed_tasks)} completed tasks deleted successfully"}
