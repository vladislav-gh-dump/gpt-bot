import asyncio
import logging
from aiogram import Bot, Dispatcher

from core.config import CONFIG
from core.router import router


async def main():
    bot = Bot(token=CONFIG['BOT_TOKEN'], parse_mode="HTML")
    dp = Dispatcher()
    dp.include_router(router=router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
