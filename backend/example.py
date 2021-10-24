from starlette.requests import Request
from starlette.responses import Response


async def app(scope, receive, send):
    assert scope['type'] == 'http'
    request = Request(scope, receive)
    inp = await request.form()
    content = '%s %s %s' % (request.method, inp.get("email"), inp.get("text"))
    response = Response(content, media_type='text/plain')
    await response(scope, receive, send)


