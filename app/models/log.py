from app import db
from datetime import datetime

class Log(db.Model):
    __tablename__ = "logs"

    id         = db.Column(db.Integer, primary_key=True)
    action     = db.Column(db.String(50), nullable=False)   # e.g. "create_task"
    details    = db.Column(db.Text, nullable=True)           # extra context
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id    = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "action": self.action,
            "details": self.details,
            "created_at": self.created_at.isoformat(),
            "user_id": self.user_id
        }