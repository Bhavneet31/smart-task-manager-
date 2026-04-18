from app import db
from app.models.log import Log

def write_log(user_id, action, details=None):
    log = Log(user_id=user_id, action=action, details=details)
    db.session.add(log)
    db.session.commit()
    return log

def get_user_logs(user_id):
    return Log.query.filter_by(user_id=user_id).order_by(Log.created_at.desc()).all()