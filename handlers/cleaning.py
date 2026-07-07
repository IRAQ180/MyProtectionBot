from aiogram import Router, F
from aiogram.types import Message
from database import get_rank, get_rank_level

router = Router()
MY_ID = 8183727038

@router.message(F.text.startswith("مسح "))
async def clean(message: Message):
    if message.from_user.id != MY_ID and get_rank_level(get_rank(message.from_user.id)) < 2:
        return await message.reply("عذراً، للمديرين فما فوق!")
    count = int(message.text.split(" ")[1])
    for i in range(count + 1):
        try: await message.bot.delete_message(message.chat.id, message.message_id - i)
        except: pass
