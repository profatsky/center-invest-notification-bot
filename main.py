import asyncio
import logging
import sys

import aiohttp
from aiogram import filters
from aiogram.types import Message

import config
from loader import dp, bot


async def send_message_to_admin():
    await bot.send_message(chat_id=int(config.ADMIN_ID), text='Бот запущен!')


@dp.message(filters.StateFilter(None))
async def catch_message(message: Message):
    url = config.BACKEND_API_URL + '/sync-telegram'
    body = {
        'telegram_username': message.from_user.username,
        'telegram_id': str(message.from_user.id),
        'secret_key': config.SECRET_KEY
    }
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(
                url=url,
                json=body
            ) as response:
                if response.status == 200:
                    await message.answer(
                        'Вы дали доступ Telegram-боту на отправку уведомлений от онлайн-школы'
                    )
        except aiohttp.ClientError as e:
            logging.info(f'Ошибка при отправке API-запроса: {e}')


async def main():
    await send_message_to_admin()
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
