from aiogram import Router, F
from aiogram.types import Message
from database import add_reply

router = Router()

@router.message(F.text.startswith("اضف رد "))
async def save_new_reply(message: Message):
    # نأخذ النص بعد كلمة "اضف رد "
    text = message.text.replace("اضف رد ", "").split(maxsplit=1)
    
    if len(text) < 2:
        return await message.reply("⚠️ صيغة خاطئة! استخدم:\nاضف رد [الكلمة] [الرد]")
    
    key, value = text[0], text[1]
    
    # حفظ في قاعدة البيانات
    add_reply(key, value)
    await message.reply(f"✅ تم حفظ الرد:\nعندما يكتب أحد: {key}\nسأرد بـ: {value}")
