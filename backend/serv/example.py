import base64
import os.path
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Route
from backend.serv.online_data import all_online
from starlette.authentication import (
    AuthenticationBackend,
    SimpleUser,
    AuthCredentials
)
from starlette.middleware import Middleware
from starlette.applications import Starlette
from starlette.authentication import requires
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.responses import JSONResponse
from starlette_auth_toolkit.cryptography import PBKDF2Hasher
from datetime import datetime, timedelta

path = os.path.dirname(__file__)
sanya = base64.b64encode(open(os.path.join(path, "../Pics/Sanya.jpg"), "rb").read()).decode("UTF-8")

online = dict()

users = [
    {
        "email": "artm-porjad@mail.ru",
        "login": "Archi",
        "password": "123",
        # "img": misha,
    }
]

quotes = []
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
    online[login] = {"user_data": {"login": login, "img": sanya}, "expired": datetime.now()}
    users.append(user)
    response = Response(status_code=200)
    response.set_cookie("auth", login, 300)
    return response


async def enter(request: Request):
    data_forms_ent = await request.form()
    login = data_forms_ent.get("login")
    password = data_forms_ent.get("password")
    for user in users:
        if user["login"] == login and user["password"] == password:
            response = Response(status_code=200)
            online[login] = {"user_data": {"login": login, "img": sanya}, "expired": datetime.now()}
            response.set_cookie("auth", login, 300)
            return response
    return JSONResponse({"error": "Пользователь или пароль не найден"}, status_code=404)


@requires('authenticated')
async def check_user(request):
    response = Response(status_code=200)
    response.set_cookie("auth", request.user.display_name, 300)
    online[request.user.display_name]["expired"] = datetime.now()
    return response

@requires('authenticated')
async def exit(request):
    del online[request.user.display_name]
    response = Response(status_code=200)
    response.delete_cookie("auth")
    return response


class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, request):
        if not request.cookies.get("auth"):
            return
        login = request.cookies.get("auth")
        return AuthCredentials(["authenticated"]), SimpleUser(login)


async def quotef(request):
    data_forms_ent = await request.form()
    text = data_forms_ent.get("text")
    quote = {
        "text": text,
        "login": request.user.display_name,
        "img": sanya,
    }
    quotes.append(quote)



async def comment_json_view(request):
    return JSONResponse(quotes)


async def online_json_view(request):
    online_send = []
    if request.user:
        for i in range(len(online)):
            if datetime.now()-online[request.user.display_name]['expired'] < timedelta(seconds=300):
                online_send.append(online[request.user.display_name]['user_data'])
    return JSONResponse(online_send)


routes = [
    Route("/api/enter", endpoint=enter, methods=["POST"]),
    Route("/api/registration", endpoint=registration, methods=["POST"]),
    Route("/api/quote", endpoint=quotef, methods=["POST"]),
    Route("/api/online_view", endpoint=online_json_view, methods=["GET"]),
    Route("/api/check_user", endpoint=check_user, methods=["GET"]),
    Route("/api/exit", endpoint=exit, methods=["GET"]),
    Route("/api/comment_view", endpoint=comment_json_view, methods=["GET"])
]

middleware = [
    Middleware(AuthenticationMiddleware, backend=BasicAuthBackend())
]

app = Starlette(routes=routes, middleware=middleware)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
