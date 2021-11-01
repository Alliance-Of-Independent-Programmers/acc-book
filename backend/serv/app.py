import typing

from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from starlette.routing import Route
from starlette.applications import Starlette
from starlette.authentication import requires
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.responses import JSONResponse, PlainTextResponse
from starlette.routing import Route

from starlette_auth_toolkit.base.backends import BaseBasicAuth
from starlette_auth_toolkit.cryptography import PBKDF2Hasher

# Password hasher
hasher = PBKDF2Hasher()


# Example user model
class User(typing.NamedTuple):
    username: str
    password: str


# Fake user storage
USERS = {
    "alice": User(username="alice", password=hasher.make_sync("alicepwd")),
    "bob": User(username="bob", password=hasher.make_sync("bobpwd")),
}

# Authentication backend
class BasicAuth(BaseBasicAuth):
    async def find_user(self, username: str):
        return USERS.get(username)

    async def verify_password(self, user: User, password: str):
        return await hasher.verify(password, user.password)


@requires("authenticated")
async def protected(request):
    return JSONResponse({"message": f"Hello, {request.user.username}!"})

routes = [
    Route("/protected", endpoint=protected, methods=["GET"]),
]

app = Starlette(routes=routes)
app.add_middleware(
    AuthenticationMiddleware,
    backend=BasicAuth(),
    on_error=lambda _, exc: PlainTextResponse(str(exc), status_code=401),
)
# app = Starlette()
#
# app.add_middleware(
#     AuthenticationMiddleware,
#     backend=BasicAuth(),
#     on_error=lambda _, exc: PlainTextResponse(str(exc), status_code=401),
# )
#
#
# @app.route("/protected")
# @requires("authenticated")
# async def protected(request):
#     return JSONResponse({"message": f"Hello, {request.user.username}!"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)