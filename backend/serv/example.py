import base64
import os.path
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from starlette.routing import Route
from starlette.applications import Starlette
from backend.serv.online_data import all_online
from backend.serv.comment_data import all_comment

path=os.path.dirname(__file__)

users = []
a = []
flag = False
misha = base64.b64encode(open(os.path.join(path, "../Pics/Miahs.jpg"), "rb").read()).decode("UTF-8")
#

async def registration(request: Request):
    data_forms_reg = await request.form()
    login = data_forms_reg.get("login")
    password = data_forms_reg.get("password")
    # img = data_forms.get("img")
    user = {
        "login": login,
        "password": password,
        # "img": misha,
        }
    users.append(user)
    print(users)
    return Response(status_code=200)


async def enter(request: Request):
    data_forms_ent = await request.form()
    login = data_forms_ent.get("login")
    password = data_forms_ent.get("password")
    # img = data_forms.get("img")
    n = len(users)
    for i in range(n):
        if users[i]["login"] == login and users[i]["password"] == password:
            a.append("accepted")
            break
    return Response(status_code=200)


async def accepted_enter_jsonrespons(request):
    print(a)
    if a[0] == "accepted":
        return JSONResponse("Пользователь найден")
    else:
        return JSONResponse("Пользователь не найден")



async def comment_json_view(request):
    return JSONResponse(all_comment)


async def online_json_view(request):
    return JSONResponse(all_online)


routes = [
    Route("/api/enter", endpoint=enter, methods=["POST"]),
    Route("/api/registration", endpoint=registration, methods=["POST"]),
    Route("/api/online_view", endpoint=online_json_view, methods=["GET"]),
    Route("/api/accepted_enter_jsonrespons", endpoint=accepted_enter_jsonrespons, methods=["GET"]),
    Route("/api/comment_view", endpoint=comment_json_view, methods=["GET"])
]

app = Starlette(routes=routes)
