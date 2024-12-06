import bcrypt


class BadPassword(Exception):
    pass


def hash(password: str) -> str:
    return bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
    ).decode('utf-8')


def check(given: str, actual: str):
    if not bcrypt.checkpw(
        given.encode('utf-8'),
        actual.encode('utf-8')
    ):
        raise BadPassword()
