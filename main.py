import asyncio
from aiogram import Bot, Dispatcher
from handlers import admin, protection

# ضع التوكن الخاص بك هنا
# نصيحة: يفضل مستقبلاً استخدام متغيرات البيئة (Environment Variables)
TOKEN = "8201679973:AAFa6xGpxL7PxXX3s1QbNEXkMjy5Ah6kvcM"

async def main():
    # إعداد البوت والـ Dispatcher
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    
    # تسجيل الـ Routers (هنا يتم ربط ملفاتك)
    dp.include_router(admin.router)
    dp.include_router(protection.router)
    
    print("البوت يعمل الآن ومستعد للحماية...")
    
    # بدء تشغيل البوت
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("تم إيقاف البوت")
