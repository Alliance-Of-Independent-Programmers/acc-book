import json
from dblib import DataBaseResolver
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

resolver = DataBaseResolver()


# Main application code.
async def list_notes(request):
    return json.dumps(resolver.get_all_users())


async def add_note(request):
    data = await request.json()
    resolver.add_user_to_db(data["nickname"], data["email"], data["password"])
    return JSONResponse({
        "text": data["nickname"],
        "completed": data["completed"]
    })


routes = [
    Route("/notes", endpoint=list_notes, methods=["GET"]),
    Route("/notes", endpoint=add_note, methods=["POST"]),
]


app = Starlette(
    routes=routes
)
