from aiogram import Bot
from aiogram.types import Message

from core.utils.api_gpt import get_content


async def command_start(message: Message, bot: Bot):
    user_first_name = message.from_user.first_name
    chat_id = message.from_user.id

    await bot.send_message(chat_id, f"Привет, {user_first_name}!\n" +
                           f"Благодарю тебя за то, что решил воспользоваться ботом BotGPT.\n" +
                           f"Напиши боту сообщение.")


async def send_message(message: Message, bot: Bot):
    user_first_name = message.from_user.first_name
    chat_id = message.from_user.id

    bot_message = await bot.send_message(chat_id, 'Ответ может занять некоторое время...')

    content = get_content([
        {'role': 'system', 'content': f"{user_first_name} отправил тебе сообщение."},
        {'role': 'user', 'content': message.text}
    ])

    await bot_message.delete()
    await bot.send_message(chat_id, content)
