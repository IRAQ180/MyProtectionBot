from aiogram import Bot, Dispatcher
import asyncio
# تأكد من إضافة info هنا
from handlers import admin, cleaning, protection, info 

async def main():
    bot = Bot(token="8201679973:AAFa6xGpxL7PxXX3s1QbNEXkMjy5Ah6kvcM") 
    dp = Dispatcher()
    
    # سجل info في الروترات
    dp.include_routers(admin.router, cleaning.router, protection.router, info.router)
    
    print("البوت يعمل الآن بنجاح...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
