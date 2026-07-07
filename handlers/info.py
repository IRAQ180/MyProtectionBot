from aiogram import Router, F
from aiogram.types import Message
from database import get_rank

router = Router()

@router.message(F.text == "ايدي")
async def get_user_info(message: Message):
    user = message.reply_to_message.from_user if message.reply_to_message else message.from_user
    rank = get_rank(user.id)
    
    # تحديد الرتبة الخاصة بك (المطور الأساسي)
    if user.id == 8183727038: rank = "المطور الأساسي"
    
    info_text = (
        f"☆-user : @{user.username or 'لا يوجد'}\n"
        f"☆-id : {user.id}\n"
        f"☆-الاسم : {user.full_name}\n"
        f"☆-الرتبة : {rank}"
    )
    
    try:
        photos = await message.bot.get_user_profile_photos(user_id=user.id, limit=1)
        if photos.total_count > 0:
            await message.reply_photo(photo=photos.photos[0][-1].file_id, caption=info_text)
        else:
            await message.reply(info_text)
    except:
        await message.reply(info_text)
