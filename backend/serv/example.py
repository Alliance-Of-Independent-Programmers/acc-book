from starlette.applications import Starlette
from starlette.authentication import (
    AuthenticationBackend, AuthenticationError, SimpleUser, UnauthenticatedUser,
    AuthCredentials
)
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.responses import PlainTextResponse
from starlette.routing import Route
import base64
import binascii
import base64
import os.path
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from starlette.routing import Route
from starlette.applications import Starlette
from backend.serv.online_data import all_online
from backend.serv.comment_data import all_comment
from starlette.authentication import (
    AuthenticationBackend, AuthenticationError, SimpleUser, UnauthenticatedUser,
    AuthCredentials
)
from starlette.middleware import Middleware
import typing
from starlette.applications import Starlette
from starlette.authentication import requires
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.responses import JSONResponse, PlainTextResponse
from starlette_auth_toolkit.base.backends import BaseBasicAuth
from starlette_auth_toolkit.cryptography import PBKDF2Hasher

path = os.path.dirname(__file__)

users = [
    {
        "email": "artm-porjad@mail.ru",
        "password": "123",
        # "img": misha,
    }
]
hasher = PBKDF2Hasher()


async def registration(request: Request):
    data_forms_reg = await request.form()
    email = data_forms_reg.get("email")
    login = data_forms_reg.get("login")
    password = data_forms_reg.get("password")
    # img = data_forms.get("img")
    user = {
        "email": email,
        "login": login,
        "password": password,
        # "img": misha,
    }
    users.append(user)
    print(users)
    return Response(status_code=200)


async def enter(request: Request):
    data_forms_ent = await request.form()
    email = data_forms_ent.get("email")
    password = data_forms_ent.get("password")
    for user in users:
        if user["email"] == email and user["password"] == password:
            response = Response(status_code=200)
            response.set_cookie("auth", email, 300)
            return response
    return JSONResponse({"error": "Пользователь или пароль не найден"}, status_code=404)


@requires('authenticated')
async def check_user(request):
    response = Response(status_code=200)
    response.set_cookie("auth", request.user.display_name, 300)
    return response


class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, request):
        print(request.cookies.get("auth"))
        if not request.cookies.get("auth"):
            return
        email = request.cookies.get("auth")
        return AuthCredentials(["authenticated"]), SimpleUser(email)


async def comment_json_view(request):
    return JSONResponse(all_comment)


async def online_json_view(request):
    return JSONResponse(all_online)


routes = [
    Route("/api/enter", endpoint=enter, methods=["POST"]),
    Route("/api/registration", endpoint=registration, methods=["POST"]),
    Route("/api/online_view", endpoint=online_json_view, methods=["GET"]),
    Route("/api/check_user", endpoint=check_user, methods=["GET"]),
    Route("/api/comment_view", endpoint=comment_json_view, methods=["GET"])
]

middleware = [
    Middleware(AuthenticationMiddleware, backend=BasicAuthBackend())
]

app = Starlette(routes=routes, middleware=middleware)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)