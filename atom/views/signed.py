from flask import request
from uuid import UUID

from atom.models import SessionQueries, UserQueries

def signed_in():
    cookies = request.cookies

    session_uuid = cookies.get('session')
    user_uuid = cookies.get('user')

    session = SessionQueries.get_by_uuid(uuid=session_uuid)

    if not session:
        return False
    
    if UUID(user_uuid) != session.user_uuid:
        return False
    
    user = UserQueries.get_by_uuid(user_uuid)
    request.user = user

    return True