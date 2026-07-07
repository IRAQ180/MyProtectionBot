from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "ايدي")
async def get_user_info(message: Message):
    # تحديد المستخدم (سواء كان الشخص المردود عليه أو المرسل)
    user = message.reply_to_message.from_user if message.reply_to_message else message.from_user
    
    # تحضير النص
    info_text = (
        f"☆-user : @{user.username or 'لا يوجد'}\n"
        f"☆-id : {user.id}\n"
        f"☆-الاسم : {user.full_name}\n"
        f"☆-الحالة : عضو في المجموعة"
    )
    
    # محاولة جلب صورة البروفايل
    try:
        photos = await message.bot.get_user_profile_photos(user_id=user.id, limit=1)
        
        # إذا وجدت صورة، أرسلها مع النص
        if photos.total_count > 0:
            photo_id = photos.photos[0][-1].file_id
            await message.reply_photo(photo=photo_id, caption=info_text)
        else:
            # إذا لم توجد صورة، أرسل النص فقط
            await message.reply(info_text)
            
    except Exception as e:
        # في حال حدوث أي خطأ تقني، أرسل النص فقط
        await message.reply(info_text)
