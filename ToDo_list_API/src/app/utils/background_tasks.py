from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from app.models import Task
from app.database import SessionLocal

def clean_completed_tasks():
    with SessionLocal() as db:
        db.query(Task).filter(Task.completed == True).delete()
        db.commit()

scheduler = BackgroundScheduler()
scheduler.add_job(clean_completed_tasks, "interval", minutes=10)
