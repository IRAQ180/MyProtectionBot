from aiogram import Bot, Dispatcher
import asyncio
from handlers import info, admin, protection, cleaning

# إعداد البوت
# ضع التوكن الخاص ببوتك بين علامتي التنصيص بدلاً من النص الموجود
TOKEN = "8201679973:AAFa6xGpxL7PxXX3s1QbNEXkMjy5Ah6kvcM"

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    
    # تسجيل جميع ملفات الأوامر (Handlers)
    dp.include_router(info.router)
    dp.include_router(admin.router)
    dp.include_router(protection.router)
    dp.include_router(cleaning.router)
    
    print("البوت يعمل الآن بنجاح...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    # تشغيل البوت
    asyncio.run(main())
