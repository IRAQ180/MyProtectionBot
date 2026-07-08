import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
# استيراد الروترات
from handlers import admin, protection, info, reply, add_reply, dev

async def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("خطأ: لم يتم العثور على BOT_TOKEN في المتغيرات!")
        return

    bot = Bot(token=token)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    # تم وضع dev.router في أول القائمة ليأخذ الأولوية
    dp.include_routers(
        dev.router,
        admin.router, 
        protection.router, 
        info.router, 
        add_reply.router,
        reply.router
    )
    
    print("--- البوت يعمل الآن وبانتظار الأوامر ---")
    
    await bot.delete_webhook(drop_pending_updates=True)
    
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("تم إيقاف البوت")
