from fastapi import APIRouter, HTTPException, Response, Cookie
from auth.models import UserCreate, UserGet, UserLogin
from auth.utils import password as psw_util
from auth.utils import jwt as jwt_util
from models.user import User

from typing import Annotated
from peewee import IntegrityError


router = APIRouter()


@router.post("/register")
def register(user: UserCreate) -> UserGet:
    user_dict = user.__dict__

    user_dict['password_hash'] = psw_util.hash(user_dict['password'])

    user_db = User(**user.__dict__)
    try:
        user_db.save()
    except IntegrityError:
        raise HTTPException(400, detail="User already exists")

    return UserGet(**user_db.__data__)


@router.post("/login")
def login(user: UserLogin, response: Response) -> UserGet:
    try:
        user_db = User.get(User.email == user.email)
        psw_util.check(user.password, user_db.password_hash)
        token = jwt_util.issue(user)
        response.set_cookie("token", token)
        return UserGet(**user_db.__data__)
    except User.DoesNotExist:
        raise HTTPException(401, detail="No such user")
    except psw_util.BadPassword:
        raise HTTPException(401, detail="Password doesn't match")


@router.post("/me")
def me(token: Annotated[str | None, Cookie()] = None) -> UserGet:
    login_msg = "You have to be logged in"
    if not token:
        raise HTTPException(401, login_msg)
    try:
        payload = jwt_util.validate(token)
        email = payload["sub"]
        user_db = User.get(User.email == email)
        return UserGet(**user_db.__data__)
    except jwt_util.BadJWT:
        raise HTTPException(401, login_msg)


@router.post("/logout")
def logout(response: Response):
    response.delete_cookie("token")
