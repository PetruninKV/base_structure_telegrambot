from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import BufferedInputFile, Message

from config_data.config import Config, load_config

from lexicon.lexicon import LEXICON_MESSAGE

config: Config = load_config()

router: Router = Router()


@router.message(CommandStart())
async def proc_statr_command(message: Message):
    pass