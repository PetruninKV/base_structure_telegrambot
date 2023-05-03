from aiogram import Router, F
from aiogram.filters import Text
from aiogram.types import Message

from lexicon.lexicon import LEXICON_MESSAGE

router: Router = Router()


@router.message(Text)
async def proc_other_mess(message: Message):
    pass
