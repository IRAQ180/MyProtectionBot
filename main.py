from aiogram import Bot, Dispatcher
import asyncio
from handlers import info, admin, protection # أضفنا protection هنا

async def main():
    bot = Bot(token="8201679973:AAFa6xGpxL7PxXX3s1QbNEXkMjy5Ah6kvcM") # ضع التوكن الخاص بك
    dp = Dispatcher()
    
    # تسجيل الملفات (Handlers)
    dp.include_router(info.router)
    dp.include_router(admin.router)
    dp.include_router(protection.router) # وأضفناها هنا
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
