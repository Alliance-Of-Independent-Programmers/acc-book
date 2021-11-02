from starlette.authentication import requires, AuthenticationBackend, AuthCredentials, SimpleUser
from starlette.middleware import Middleware

from backend.dbresolvers.userdb import UserDataResolver
from backend.dbresolvers.quotesdb import QuoteDataResolver
from starlette.applications import Starlette
from starlette.responses import JSONResponse, Response
from starlette.routing import Route
from starlette.requests import Request

from starlette.middleware.authentication import AuthenticationMiddleware

# Objects do all database manipulations
user_db_resolver = UserDataResolver()
quotes_db_resolver = QuoteDataResolver()


# Main application code.
async def get_all_users(request):
    user_list = user_db_resolver.get_all_users()
    users_json = dict()
    for user in user_list:
        user_info = {"nickname": user.nickname, "email": user.email, "password": user.password}
        users_json[user.user_id] = user_info
    return JSONResponse(users_json)


# async def add_user(request):
#     data = await request.json()
#     is_user_valid = user_db_resolver.check_user_validity(data["nickname"], data["email"])
#     print(is_user_valid)
#     if is_user_valid:
#         user_db_resolver.add_user_to_db(data["nickname"], data["email"], data["password"])
#         user_db_resolver.commit_session()
#     return JSONResponse({
#         "text": data["nickname"],
#         "status": data["success"]
#     })


async def get_all_quotes(request):
    quotes_list = quotes_db_resolver.get_all_quotes()
    quotes_json = dict()
    for quote in quotes_list:
        quote_info = {"author": quote.author, "the_quote": quote.the_quote}
        quotes_json[quote.quote_id] = quote_info
    return JSONResponse(quotes_json)


async def add_quote(request):
    data = await request.json()
    quotes_db_resolver.add_quote(data["author"], data["quote"])
    quotes_db_resolver.commit_session()
    return JSONResponse({
        "quote": data["quote"],
        "status": data["success"]
    })


async def registration(request: Request):
    data_forms_reg = await request.form()
    login = data_forms_reg.get("login")
    email = data_forms_reg.get("email")
    password = data_forms_reg.get("password")
    # TODO: get rid of possibility to add double note
    is_user_valid = user_db_resolver.check_user_validity(data_forms_reg["login"], data_forms_reg["email"])
    print(is_user_valid)
    if is_user_valid:
        user_db_resolver.add_user_to_db(login, email, password)
        user_db_resolver.commit_session()
        response = Response(status_code=200)
        response.set_cookie("auth", email, 300)
        return response
    return JSONResponse({"error": "Логин или email уже заняты"}, status_code=404)


async def enter(request: Request):
    data_forms_ent = await request.form()
    login = data_forms_ent.get("email")
    password = data_forms_ent.get("password")
    authentification_status = user_db_resolver.authentificate(login, password)
    if authentification_status:
        response = Response(status_code=200)
        response.set_cookie("auth", login, 300)
        return response
    else:
        return JSONResponse({"error": "Пользователь или пароль не найден"}, status_code=404)

# Cookies

class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, request):
        if not request.cookies.get("auth"):
            return
        email = request.cookies.get("auth")
        return AuthCredentials(["authenticated"]), SimpleUser(email)

@requires('authenticated')
async def check_user(request):
    response = Response(status_code=200)
    response.set_cookie("auth", request.user.display_name, 300)
    return response

@requires('authenticated')
async def exit(request):
    response = Response(status_code=200)
    response.delete_cookie("auth")
    return response



# TODO: needs to be tested
routes = [
    Route("/api/enter", endpoint=enter, methods=["POST"]),
    Route("/api/registration", endpoint=registration, methods=["POST"]),
    Route("/api/all_users", endpoint=get_all_users, methods=["GET"]),
    Route("/api/all_quotes", endpoint=get_all_quotes, methods=["GET"]),
    Route("/api/all_quotes", endpoint=add_quote, methods=["POST"]),
    Route("/api/check_user", endpoint=check_user, methods=["GET"]),
    Route("/api/exit", endpoint=exit, methods=["GET"]),
]

middleware = [
    Middleware(AuthenticationMiddleware, backend=BasicAuthBackend())
]

app = Starlette(
    routes=routes,
    middleware=middleware
)
