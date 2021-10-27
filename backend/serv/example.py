import base64
import os.path
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from starlette.routing import Route
from starlette.applications import Starlette
from backend.serv.online_data import all_online
from backend.serv.comment_data import all_comment

path=os.path.dirname(__file__)

a = []
misha = base64.b64encode(open(os.path.join(path, "../Pics/Miahs.jpg"), "rb").read()).decode("UTF-8")
#

async def save_comment(request: Request):
    data_forms = await request.form()
    login = data_forms.get("login")
    text = data_forms.get("text")
    img = data_forms.get("img")
    comment1 = {
        "text": text,
        "author": {
            "login": login,
            "img": misha,
        },
    }
    a.append(comment1)
    return Response(status_code=200)


async def comment1_json_view(request):
    print(a)
    return JSONResponse(a)


async def comment_json_view(request):
    return JSONResponse(all_comment)


async def online_json_view(request):
    return JSONResponse(all_online)


routes = [
    Route("/api/example/app", endpoint=save_comment, methods=["POST"]),
    Route("/api/online_view", endpoint=online_json_view, methods=["GET"]),
    Route("/api/comment1_view", endpoint=comment1_json_view, methods=["GET"]),
    Route("/api/comment_view", endpoint=comment_json_view, methods=["GET"])
]

app = Starlette(routes=routes)
