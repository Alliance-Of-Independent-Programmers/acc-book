from backend.dbresolvers.userdb import UserDataResolver
from backend.dbresolvers.quotesdb import QuoteDataResolver
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


user_db_resolver = UserDataResolver()
quotes_db_resolver = QuoteDataResolver()


# Main application code.
async def get_all_users(request):
    return JSONResponse(user_db_resolver.get_all_users())


async def add_note(request):
    data = await request.json()
    user_db_resolver.add_user_to_db(data["nickname"], data["email"], data["password"])
    user_db_resolver.commit_session()
    return JSONResponse({
        "text": data["nickname"],
        "status": data["success"]
    })


async def get_all_quotes(request):
    return JSONResponse(quotes_db_resolver.get_all_quotes())


async def add_quote(request):
    data = await request.json()
    quotes_db_resolver.add_quote(data["author"], data["quote"])
    quotes_db_resolver.commit_session()
    return JSONResponse({
        "quote": data["quote"],
        "status": data["success"]
    })


# TODO: needs to be tested
routes = [
    Route("/api/all_users", endpoint=get_all_users, methods=["GET"]),
    Route("/api/all_users", endpoint=add_note, methods=["POST"]),
    Route("/api/all_quotes", endpoint=get_all_quotes, methods=["GET"]),
    Route("/api/all_quotes", endpoint=add_quote, methods=["POST"])
]


app = Starlette(
    routes=routes
)
