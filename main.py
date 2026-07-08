import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
# استيراد جميع الهاندلرز الخاصة بك
from handlers import admin, protection, info, reply, add_reply, dev

async def main():
    # جلب التوكن من المتغيرات في Railway
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("خطأ: لم يتم العثور على BOT_TOKEN في المتغيرات!")
        return

    # إنشاء كائن البوت
    bot = Bot(token=token)
    
    # إعداد التخزين
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    # تسجيل جميع الروترات
    dp.include_routers(
        admin.router, 
        protection.router, 
        info.router, 
        add_reply.router,
        reply.router,
        dev.router
    )
    
    print("--- البوت يعمل الآن وبانتظار الأوامر ---")
    print("تم تسجيل الروترات بنجاح، بما فيها روتر المطور.")
    
    # تنظيف الأوامر المعلقة
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
