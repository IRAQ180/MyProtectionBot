from aiogram import Router, F
from aiogram.types import Message
from database import get_rank, get_rank_level

router = Router()
MY_ID = 8183727038 # آيديك الجديد

@router.message(F.text.startswith("مسح "))
async def clean_messages(message: Message):
    # إذا لم تكن أنت، نتأكد من الرتبة (مدير فما فوق)
    if message.from_user.id != MY_ID:
        if get_rank_level(get_rank(message.from_user.id)) < 2:
            return await message.reply("عذراً، هذا الأمر للمديرين فما فوق! 🚫")
    
    try:
        count = int(message.text.split(" ")[1])
        for i in range(count + 1):
            try:
                await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - i)
            except:
                pass
    except:
        await message.reply("يرجى كتابة عدد صحيح، مثال: مسح 10")
