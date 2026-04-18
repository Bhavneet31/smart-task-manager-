from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.task_service import (
    create_task, get_all_tasks, get_task,
    update_task, delete_task, mark_completed
)
from app.services.log_service import write_log

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/", methods=["POST"])
@jwt_required()
def create():
    user_id = int(get_jwt_identity())
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "title is required"}), 400

    task = create_task(
        user_id=user_id,
        title=data["title"],
        description=data.get("description"),
        priority=data.get("priority", "medium"),
        due_date=data.get("due_date")
    )
    write_log(user_id, "create_task", f"Created task '{task.title}'")
    return jsonify({"message": "Task created", "task": task.to_dict()}), 201

@task_bp.route("/", methods=["GET"])
@jwt_required()
def get_all():
    user_id = int(get_jwt_identity())
    tasks = get_all_tasks(user_id)
    return jsonify({"tasks": [t.to_dict() for t in tasks]}), 200

@task_bp.route("/<int:task_id>", methods=["GET"])
@jwt_required()
def get_one(task_id):
    user_id = int(get_jwt_identity())
    task = get_task(task_id, user_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"task": task.to_dict()}), 200

@task_bp.route("/<int:task_id>", methods=["PUT"])
@jwt_required()
def update(task_id):
    user_id = int(get_jwt_identity())
    data = request.get_json()
    task, error = update_task(task_id, user_id, data)
    if error:
        return jsonify({"error": error}), 404
    write_log(user_id, "update_task", f"Updated task '{task.title}'")
    return jsonify({"message": "Task updated", "task": task.to_dict()}), 200

@task_bp.route("/<int:task_id>", methods=["DELETE"])
@jwt_required()
def delete(task_id):
    user_id = int(get_jwt_identity())
    success, error = delete_task(task_id, user_id)
    if error:
        return jsonify({"error": error}), 404
    write_log(user_id, "delete_task", f"Deleted task #{task_id}")
    return jsonify({"message": "Task deleted"}), 200

@task_bp.route("/<int:task_id>/complete", methods=["PATCH"])
@jwt_required()
def complete(task_id):
    user_id = int(get_jwt_identity())
    task, error = mark_completed(task_id, user_id)
    if error:
        return jsonify({"error": error}), 404
    write_log(user_id, "complete_task", f"Completed task '{task.title}'")
    return jsonify({"message": "Task marked as completed", "task": task.to_dict()}), 200