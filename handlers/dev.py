from aiogram import Router, types, F
from aiogram.types import Message

# إنشاء الروتر
router = Router()

# أمر "المطور" لجلب المعلومات والصورة
@router.message(F.text == "المطور")
async def dev_info(message: Message):
    # 1. الحصول على معلومات المستخدم (المطور)
    user = message.from_user
    
    # 2. الحصول على صور البروفايل (أول صورة فقط)
    photos = await message.bot.get_user_profile_photos(user_id=user.id, limit=1)
    
    # تنسيق المعلومات
    text = (
        f"👤 المطور: {user.full_name}\n"
        f"🆔 الآيدي: `{user.id}`\n"
        f"🏷 اليوزر: @{user.username if user.username else 'لا يوجد'}"
    )

    # 3. التحقق من وجود صورة وإرسالها
    if photos.total_count > 0:
        # جلب الـ file_id لأكبر حجم من الصورة الأولى
        photo_file_id = photos.photos[0][-1].file_id
        await message.answer_photo(photo=photo_file_id, caption=text, parse_mode="Markdown")
    else:
        # إذا لم يجد صورة، يرسل النص فقط
        await message.answer(text, parse_mode="Markdown")
