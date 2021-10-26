import json
from backend.dbresolvers.userdb import UserDataResolver
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

resolver = UserDataResolver()


# Main application code.
async def get_all_users(request):
    return JSONResponse(json.dumps(resolver.get_all_users()))


async def add_note(request):
    data = await request.json()
    resolver.add_user_to_db(data["nickname"], data["email"], data["password"])
    return JSONResponse({
        "text": data["nickname"],
        "completed": data["completed"]
    })

# TODO: needs to be tested
routes = [
    Route("/api/all_users", endpoint=get_all_users, methods=["GET"]),
    Route("/api/all_users", endpoint=add_note, methods=["POST"])
]


app = Starlette(
    routes=routes
)
