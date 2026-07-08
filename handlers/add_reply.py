from aiogram import Router, F
from aiogram.types import Message
from database import add_reply

router = Router()

@router.message(F.text.startswith("اضف رد "))
async def save_new_reply(message: Message):
    # تقسيم النص إلى الكلمة والرد
    parts = message.text.split(" ", 2)
    if len(parts) < 3:
        return await message.reply("⚠️ صيغة خاطئة! استخدم:\nاضف رد [الكلمة] [الرد]")
    
    key, value = parts[1], parts[2]
    add_reply(key, value)
    await message.reply(f"✅ تم الحفظ:\nعندما يكتب أحد: {key}\nسأرد بـ: {value}")
