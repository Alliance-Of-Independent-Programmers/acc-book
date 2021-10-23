from starlette.applications import Starlette
from starlette.responses import FileResponse
from starlette.routing import Route
from starlette.staticfiles import StaticFiles


def homepage(request):
    return FileResponse('../frontend/public/index.html')

#
#def user_me(request):
#    username = "John Doe"
#    return PlainTextResponse('Hello, %s!' % username)

# def user(request):
#    username = request.path_params['username']
#    return PlainTextResponse('Hello, %s!' % username)

# async def websocket_endpoint(websocket):
#    await websocket.accept()
#    await websocket.send_text('Hello, websocket!')
#    await websocket.close()


def startup():
    print('Ready to go')


routes = [
    Route('/', homepage),
    #Route('/user/me', user_me),
    #Route('/user/{username}', user),
    #WebSocketRoute('/ws', websocket_endpoint),
    #Mount('/static', StaticFiles(directory="static")),
]

app = Starlette(debug=True, routes=routes, on_startup=[startup])