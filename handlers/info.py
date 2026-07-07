from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "ايدي")
async def get_user_info(message: Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user
        info_text = (
            f"☆-user : @{user.username or 'لا يوجد'}\n"
            f"☆-id : {user.id}\n"
            f"☆-الاسم : {user.full_name}\n"
            f"☆-الحالة : عضو في المجموعة"
        )
        await message.reply(info_text)
    else:
        user = message.from_user
        info_text = (
            f"☆-user : @{user.username or 'لا يوجد'}\n"
            f"☆-id : {user.id}\n"
            f"☆-الاسم : {user.full_name}"
        )
        await message.reply(info_text)
