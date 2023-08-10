import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_reader import config
from handlers import command


async def main():
    logging.basicConfig(  # Логирование
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    dp = Dispatcher()  # Диспетчер
    bot = Bot(config.bot_token.get_secret_value(), parse_mode="HTML")  # Определение бота через токен
    dp.include_routers(command.router)  # подключение всех роутеров, привязанных к диспетчеру

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())  # Поллинг,
    # включаем все виды запросов


if __name__ == '__main__':  # Старт работы бота
    asyncio.run(main())
