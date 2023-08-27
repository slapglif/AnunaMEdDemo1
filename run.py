"""
@author: Kuro
"""
import asyncio
import logging
import os

from py_linq import Enumerable
from uvicorn import Config, Server

from app import app
from app.endpoints.routes import add_routes
from settings import Config as config


logging.basicConfig(
    filename=f"{os.getcwd()}/logs/runtime.log",
    filemode="a",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True,
)
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

app = add_routes(app)

class WebSocketServer(Server):
    """
    This class is a wrapper around the Uvicorn Server class.
    """

    async def run(self, sockets = None):
        self.config.setup_event_loop()
        return await self.serve(sockets=sockets)

async def run():
    app_configs = [
        {
            "WebAPI": Config(
                "app:app",
                host=config.fastapi_host,
                port=config.fastapi_port,
                ssl_keyfile="certs/local.key",
                ssl_certfile="certs/local.pem",
                workers=config.workers,
            )
        },
        {
            "SocketIO": Config(
                "app.rpc:app",
                host=config.fastapi_host,
                port=config.fastapi_port + 1,
                ssl_keyfile="certs/local.key",
                ssl_certfile="certs/local.pem",
            )
        },
    ]

    apps = [
        WebSocketServer(config=Enumerable(_config.values()).first()).run()
        for _config in app_configs
    ]

    return await asyncio.gather(*apps)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
