from aiogram import Router, F
from aiogram.types import Message
from database import get_rank, get_rank_level

router = Router()

@router.message(F.text.contains("http") | F.text.contains("t.me"))
async def delete_links(message: Message):
    # التحقق: إذا كان المرسل رتبته "مدير" (مستوى 3) فما فوق، لا تحذف رسالته
    if get_rank_level(get_rank(message.from_user.id)) >= 3:
        return
    
    # حذف الرسالة إذا كان المرسل عضواً أو مميزاً
    try:
        await message.delete()
        await message.answer(f"عذراً {message.from_user.first_name}، يمنع إرسال الروابط هنا! 🚫")
    except:
        pass
