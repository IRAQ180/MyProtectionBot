from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message

# إنشاء الروتر
router = Router()

# أمر تجريبي للمطور
@router.message(Command("dev"))
async def dev_command(message: Message):
    # استخدام message.bot بدلاً من تعريف التوكن يدوياً
    # هذا يضمن أن البوت يستخدم الاتصال الحالي الموجود في main.py
    bot = message.bot
    
    # مثال: إرسال رد يؤكد أن الأوامر تعمل
    await message.answer("✅ أوامر المطور تعمل بنجاح!")

# يمكنك إضافة المزيد من الأوامر هنا بنفس الطريقة
# @router.message(Command("status"))
# async def status_command(message: Message):
#     await message.answer("البوت يعمل بشكل ممتاز على Railway!")
