import asyncio
import logging
import uvicorn

import coloredlogs

from app import db
from app.arguments import parse_arguments
from app.config import Config, parse_config
from app.db import close_orm, init_orm
from app.utils.mime import magic_status 

from app.dispatcher import dispatcher

from datetime import datetime


async def on_startup(
    disp, config: Config, **kwargs
):
    tortoise_config = config.database.get_tortoise_config()
    await init_orm(tortoise_config)

    web_config = config.web.get_config()

    logging.error("Started!")

    uvicorn.run(
        disp,
        host=web_config["host"],
        port=web_config["port"]
    )


async def on_shutdown():
    logging.warning("Stopping...")
    await close_orm()


async def main():
    coloredlogs.install(level=logging.INFO)
    logging.warning("Starting...")

    arguments = parse_arguments()
    config = parse_config(arguments.config)

    tortoise_config = config.database.get_tortoise_config()
    try:
        await db.create_models(tortoise_config)
    except FileExistsError:
        await db.migrate_models(tortoise_config)

    start_time = datetime.now()

    context_kwargs = {
        "start_time": start_time,
        "magic_status": magic_status,
    }

    disp = dispatcher(context_kwargs)

    await on_startup(disp, config, **context_kwargs)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        asyncio.run(on_shutdown())
        logging.error("Stopped!")
