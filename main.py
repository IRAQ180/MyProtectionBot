import asyncio
from aiogram import Bot, Dispatcher
from handlers import admin, protection, info

# ضع التوكن الخاص بك هنا
TOKEN = "8201679973:AAFa6xGpxL7PxXX3s1QbNEXkMjy5Ah6kvcM"

async def main():
    # إعداد البوت
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    
    # ربط جميع ملفات الـ Handlers
    dp.include_router(admin.router)
    dp.include_router(protection.router)
    dp.include_router(info.router)
    
    print("البوت يعمل الآن ومستعد لكل المهام...")
    
    # بدء تشغيل البوت
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("تم إيقاف البوت")
