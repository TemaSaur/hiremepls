import jwt
import datetime


SECRET = "supersecretkey"
ALGORITHMS = ["HS256"]
TTL = datetime.timedelta(days=30)


class BadJWT(Exception):
    pass


def issue(user) -> str:
    exp = datetime.datetime.utcnow() + TTL
    data = {
        "sub": user.email,
        "exp": exp
    }
    return jwt.encode(data, SECRET, ALGORITHMS[0])


def validate(token: str):
    try:
        return jwt.decode(token)
    except Exception:
        raise BadJWT()
