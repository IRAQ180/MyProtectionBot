from aiogram import Router, F
from aiogram.types import Message

router = Router()

# هنا نضع قائمة الرتب (يمكنك إضافة أي ID لأي شخص)
RANKS = {
    8274438598: "المطور الأساسي", # ضع هنا الـ ID الخاص بك
    123456789: "مطور ثانوي",      # يمكنك إضافة أصدقائك هنا
    987654321: "مالك",
}

async def get_rank(message: Message, user_id: int) -> str:
    # 1. التحقق أولاً من القائمة التي حددناها بالأعلى
    if user_id in RANKS:
        return RANKS[user_id]
    
    # 2. التحقق من صلاحيات تليجرام التلقائية
    member = await message.bot.get_chat_member(message.chat.id, user_id)
    if member.status == 'creator':
        return "منشئ المجموعة"
    elif member.status == 'administrator':
        return "مدير"
    else:
        return "عضو"

@router.message(F.text == "ايدي")
async def get_user_info(message: Message):
    user = message.reply_to_message.from_user if message.reply_to_message else message.from_user
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
            await message.reply_photo(photo=photos.photos[0][-1].file_id, caption=info_text)
        else:
            await message.reply(info_text)
    except:
        await message.reply(info_text)
