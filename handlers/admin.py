from aiogram import Router, F
from aiogram.types import Message
from database import set_rank, remove_rank

router = Router()

ranks_list = ["مميز", "مدير", "منشئ", "منشئ اساسي", "مالك", "مطور", "مطور ثانوي", "مطور اساسي"]

@router.message(F.text.startswith("رفع "))
async def promote(message: Message):
    if message.reply_to_message:
        rank = message.text.replace("رفع ", "")
        if rank in ranks_list:
            set_rank(message.reply_to_message.from_user.id, rank)
            await message.reply(f"تم رفع العضو إلى رتبة [{rank}] بنجاح ✅")

@router.message(F.text.startswith("تنزيل "))
async def demote(message: Message):
    if message.reply_to_message:
        remove_rank(message.reply_to_message.from_user.id)
        await message.reply("تم تنزيل العضو إلى رتبة [عضو] بنجاح ⚠️")
