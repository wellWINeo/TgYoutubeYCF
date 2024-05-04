from update_handler import handle_update
from aiohttp import web
from dotenv import load_dotenv
from ycf import YCF


async def handler(event, context):
    load_dotenv(".env.dev")
    print(event)

    await handle_update(event)

    return {'statusCode': 200}


if __name__ == "__main__":
    YCF.runningOutside()

    async def internal_handler(request: web.Request) -> web.StreamResponse:
        json = await request.json()

        try:
            await handler(json, None)
            return web.Response(status=200, text="OK")
        except Exception as ex:
            print(ex)
            return web.Response(status=500, text="Internal Server Error")

    app = web.Application()
    app.router.add_post("/", internal_handler)

    print("Listening 7080...")
    web.run_app(app, port=7080)
