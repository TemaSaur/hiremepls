from fastapi import Cookie, Header, HTTPException, Depends
from typing import Annotated
from peewee import DoesNotExist

from auth.utils import jwt as jwt_util
from db.models.user import User


def get_token(
    token: Annotated[str | None, Cookie()] = None,
    authorization: Annotated[str | None, Header()] = None,
) -> str:
    jwt = token or authorization
    if not jwt:
        raise HTTPException(401, "You have to be authorized")
    return jwt


def get_user(token=Depends(get_token)) -> User:
    try:
        email = jwt_util.validate(token)['sub']
        user_db = User.get(User.email == email)
        return user_db
    except jwt_util.BadJWT:
        raise HTTPException(401, "You have to be authorized")
    except DoesNotExist:
        raise HTTPException(401, "User does not exist")
