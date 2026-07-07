from aiogram import Router, F
from aiogram.types import Message
from database import set_rank, remove_rank, get_rank, get_rank_level

router = Router()

@router.message(F.text.startswith("رفع "))
async def promote(message: Message):
    if not message.reply_to_message: return await message.reply("يرجى الرد على الشخص!")
    
    # التحقق: لا يرفع إلا المطور (مستوى 7 فما فوق)
    if get_rank_level(get_rank(message.from_user.id)) < 7:
        return await message.reply("عذراً، هذا الأمر للمطورين فقط! 🚫")

    rank = message.text.replace("رفع ", "")
    set_rank(message.reply_to_message.from_user.id, rank)
    await message.reply(f"تم رفع العضو إلى رتبة [{rank}] بنجاح ✅")

@router.message(F.text.startswith("تنزيل "))
async def demote(message: Message):
    if not message.reply_to_message: return await message.reply("يرجى الرد على الشخص!")
    
    if get_rank_level(get_rank(message.from_user.id)) < 7:
        return await message.reply("عذراً، هذا الأمر للمطورين فقط! 🚫")

    remove_rank(message.reply_to_message.from_user.id)
    await message.reply("تم تنزيل العضو إلى رتبة [عضو] بنجاح ⚠️")
