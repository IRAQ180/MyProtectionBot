from aiogram import Router, F
from aiogram.types import Message
from database import get_rank, get_rank_level

router = Router()
MY_ID = 8183727038 # آيديك الثابت

@router.message(F.text.startswith("طرد"))
async def ban_user(message: Message):
    # 1. إذا كنت أنت (المطور الأساسي) نفذ فوراً
    if message.from_user.id == MY_ID:
        if message.reply_to_message:
            await message.reply("تم طرد العضو بنجاح ✅")
            return
        return await message.reply("يرجى الرد على الشخص الذي تريد طرده!")

    # 2. إذا لم تكن أنت، تحقق من الرتبة (لا يطرد إلا مدير فما فوق)
    user_rank = get_rank(message.from_user.id)
    if get_rank_level(user_rank) < 2:
        return await message.reply("عذراً، هذا الأمر للمديرين فما فوق! 🚫")
    
    if not message.reply_to_message:
        return await message.reply("يرجى الرد على العضو!")
        
    await message.reply("تم طرد العضو بنجاح ✅")
