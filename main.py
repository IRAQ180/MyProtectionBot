from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from handlers import admin, protection, info, reply, add_reply, dev

async def main():
    # ضع التوكن الخاص ببوتك هنا
    bot = Bot(token="8201679973:AAFa6xGpxL7PxXX3s1QbNEXkMjy5Ah6kvcM") 
    
    # إعداد التخزين المؤقت للمحادثات
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    # تسجيل جميع الملفات (الروترات)
    dp.include_routers(
        admin.router, 
        protection.router, 
        info.router, 
        add_reply.router,
        reply.router,
        dev.router
    )
    
    print("البوت يعمل الآن بكامل الميزات...")
    
    # الحل الجذري لمشكلة ConflictError: 
    # مسح الـ Webhook القديم وإلغاء أي جلسة معلقة في سيرفرات تليجرام
    await bot.delete_webhook(drop_pending_updates=True)
    
    # تشغيل البوت
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("تم إيقاف البوت")
