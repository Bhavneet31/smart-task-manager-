from app import db
from app.models.task import Task
from datetime import datetime

def create_task(user_id, title, description=None, priority="medium", due_date=None):
    task = Task(
        title=title,
        description=description,
        priority=priority,
        due_date=datetime.fromisoformat(due_date) if due_date else None,
        user_id=user_id
    )
    db.session.add(task)
    db.session.commit()
    return task

def get_all_tasks(user_id):
    return Task.query.filter_by(user_id=user_id).all()

def get_task(task_id, user_id):
    return Task.query.filter_by(id=task_id, user_id=user_id).first()

def update_task(task_id, user_id, data):
    task = get_task(task_id, user_id)
    if not task:
        return None, "Task not found"

    if "title" in data:
        task.title = data["title"]
    if "description" in data:
        task.description = data["description"]
    if "priority" in data:
        task.priority = data["priority"]
    if "due_date" in data:
        task.due_date = datetime.fromisoformat(data["due_date"]) if data["due_date"] else None

    task.updated_at = datetime.utcnow()
    db.session.commit()
    return task, None

def delete_task(task_id, user_id):
    task = get_task(task_id, user_id)
    if not task:
        return False, "Task not found"
    db.session.delete(task)
    db.session.commit()
    return True, None

def mark_completed(task_id, user_id):
    task = get_task(task_id, user_id)
    if not task:
        return None, "Task not found"
    task.is_completed = True
    task.updated_at = datetime.utcnow()
    db.session.commit()
    return task, None