from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from starlette.routing import Route
from starlette.applications import Starlette
from backend.serv.online_data import all_online


async def save_comment(request: Request):
    data_forms = await request.form()
    email = data_forms.get("email")
    text = data_forms.get("text")
    print(email, text)
    return Response(status_code=200)


async def json_view(request):
    return JSONResponse(all_online)


routes=[
    Route("/api/example/app", endpoint=save_comment, methods=["POST"]),
    Route("/api/online_view", endpoint=json_view, methods=["GET"])
]

app = Starlette(routes=routes)
