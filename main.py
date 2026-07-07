
from aiogram import Bot, Dispatcher
import asyncio
from handlers import admin, cleaning, protection, info

async def main():
    # ضع التوكن الجديد هنا بعد تغييره من BotFather
    bot = Bot(token="8201679973:AAFa6xGpxL7PxXX3s1QbNEXkMjy5Ah6kvcM") 
    dp = Dispatcher()
    
    dp.include_routers(admin.router, cleaning.router, protection.router, info.router)
    
    print("البوت يعمل الآن...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
