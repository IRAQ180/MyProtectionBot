from aiogram import Router, F
from aiogram.types import Message
from database import set_rank, remove_rank, get_rank, get_rank_level

router = Router()
MY_ID = 8183727038

@router.message(F.text.startswith("رفع "))
async def promote(message: Message):
    if not message.reply_to_message: return await message.reply("يرجى الرد على العضو!")
    if message.from_user.id != MY_ID and get_rank_level(get_rank(message.from_user.id)) < 7:
        return await message.reply("عذراً، هذا للمطورين فقط!")
    rank = message.text.replace("رفع ", "")
    set_rank(message.reply_to_message.from_user.id, rank)
    await message.reply(f"تم رفع العضو إلى [{rank}]")
