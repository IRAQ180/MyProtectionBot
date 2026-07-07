from aiogram import Router, F
from aiogram.types import Message

router = Router()

# دالة لاكتشاف الروابط وحذفها
@router.message(F.text.regexp(r"(http|https|www|t\.me)"))
async def delete_links(message: Message):
    # يقوم البوت بحذف الرسالة التي تحتوي على رابط
    await message.delete()
    # يرسل تنبيهاً بسيطاً
    await message.answer(f"عذراً {message.from_user.first_name}، يمنع إرسال الروابط في هذه المجموعة.")

