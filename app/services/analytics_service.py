from app.models.task import Task

def get_analytics(user_id):
    total     = Task.query.filter_by(user_id=user_id).count()
    completed = Task.query.filter_by(user_id=user_id, is_completed=True).count()
    pending   = total - completed
    percentage = round((completed / total * 100), 2) if total > 0 else 0.0

    return {
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": pending,
        "completion_percentage": percentage
    }