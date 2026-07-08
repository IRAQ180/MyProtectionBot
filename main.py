from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from handlers import admin, protection, info, reply, add_reply

async def main():
    # ضع التوكن الخاص ببوتك هنا
    bot = Bot(token="8201679973:AAFa6xGpxL7PxXX3s1QbNEXkMjy5Ah6kvcM") 
    
    # إعداد التخزين المؤقت للمحادثات (FSM)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    # تسجيل جميع الروترات
    dp.include_routers(
        admin.router, 
        protection.router, 
        info.router, 
        reply.router, 
        add_reply.router
    )
    
    print("البوت يعمل الآن بكامل الميزات وبدعم المحادثة...")
    
    # حذف التحديثات القديمة عند بدء التشغيل
    await bot.delete_webhook(drop_pending_updates=True)
    
    # تشغيل البوت
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
