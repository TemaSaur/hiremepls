from fastapi import APIRouter, HTTPException, Response
from auth.models import UserCreate, UserGet, UserLogin
from auth.utils import password as psw_util
from auth.utils import jwt as jwt_util
from models.user import User

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
