from aiogram import Router, F
from aiogram.types import Message
from database import get_rank, get_rank_level

router = Router()

# أمر مسح عدد معين من الرسائل (مثلاً: مسح 10)
@router.message(F.text.startswith("مسح "))
async def clean_messages(message: Message):
    # التحقق: لا يمسح إلا مدير (مستوى 3) فما فوق
    if get_rank_level(get_rank(message.from_user.id)) < 3:
        return await message.reply("عذراً، هذا الأمر للمديرين فما فوق! 🚫")
    
    try:
        # استخراج العدد من الرسالة
        count = int(message.text.split(" ")[1])
        
        # مسح الرسائل
        for i in range(count + 1): # +1 لمسح أمر "مسح" نفسه
            try:
                await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - i)
            except:
                pass
    except:
        await message.reply("يرجى كتابة عدد صحيح، مثال: مسح 10")
