from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsPhotoDoc(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, str]:
        pass
