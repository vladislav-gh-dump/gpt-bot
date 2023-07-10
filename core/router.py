from aiogram import Router
from aiogram.filters import Command
from core.handlers.basic import command_start, send_message


router = Router()

router.message.register(command_start, Command(commands=["start", "run"]))
router.message.register(send_message)
