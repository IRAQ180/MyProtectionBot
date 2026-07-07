from aiogram import Router, F
from aiogram.types import Message
from database import get_rank

router = Router()

@router.message(F.text == "ايدي")
async def get_user_info(message: Message):
    user = message.reply_to_message.from_user if message.reply_to_message else message.from_user
    rank = get_rank(user.id)
    if user.id == 8183727038:
        rank = "المطور الأساسي"
    
    text = (
        f"☆-user : @{user.username or 'لا يوجد'}\n"
        f"☆-id : {user.id}\n"
        f"☆-الاسم : {user.full_name}\n"
        f"☆-الرتبة : {rank}"
    )
    await message.reply(text)
