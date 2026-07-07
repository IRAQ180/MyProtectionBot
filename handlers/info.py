from aiogram import Router, F
from aiogram.types import Message

router = Router()

# ضع الـ ID الخاص بك هنا لتعريفك كـ "المطور"
OWNER_ID = 8274438598 

async def get_rank(message: Message, user_id: int) -> str:
    # التحقق من صلاحيات العضو في المجموعة
    member = await message.bot.get_chat_member(message.chat.id, user_id)
    
    if user_id == OWNER_ID:
        return "المطور الأساسي"
    elif member.status in ['creator', 'administrator']:
        return "مشرف"
    else:
        return "عضو"

@router.message(F.text == "ايدي")
async def get_user_info(message: Message):
    user = message.reply_to_message.from_user if message.reply_to_message else message.from_user
    
    # الحصول على الرتبة
    rank = await get_rank(message, user.id)
    
    info_text = (
        f"☆-user : @{user.username or 'لا يوجد'}\n"
        f"☆-id : {user.id}\n"
        f"☆-الاسم : {user.full_name}\n"
        f"☆-الرتبة : {rank}"
    )
    
    try:
        photos = await message.bot.get_user_profile_photos(user_id=user.id, limit=1)
        if photos.total_count > 0:
            photo_id = photos.photos[0][-1].file_id
            await message.reply_photo(photo=photo_id, caption=info_text)
        else:
            await message.reply(info_text)
    except:
        await message.reply(info_text)
