from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "Task Manager API with database is running"}


@app.post("/tasks")
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    new_task = models.Task(
        title=task.title,
        completed=task.completed
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    return task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()

    db_task.title = task.title
    db_task.completed = task.completed

    db.commit()
    db.refresh(db_task)

    return db_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()

    db.delete(db_task)
    db.commit()

    return {"message": "Task deleted"}