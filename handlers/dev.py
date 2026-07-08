from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

# إنشاء الروتر
router = Router()

# هذا الهاندلر يستجيب حصراً للكلمة "المطور"
@router.message(F.text == "المطور")
async def dev_info(message: Message):
    user = message.from_user
    
    # جلب صورة البروفايل
    photos = await message.bot.get_user_profile_photos(user_id=user.id, limit=1)
    
    text = (
        f"👤 المطور: {user.full_name}\n"
        f"🆔 الآيدي: `{user.id}`\n"
        f"🏷 اليوزر: @{user.username if user.username else 'لا يوجد'}"
    )

    # إرسال الصورة إذا توفرت
    if photos.total_count > 0:
        photo_file_id = photos.photos[0][-1].file_id
        await message.answer_photo(photo=photo_file_id, caption=text, parse_mode="Markdown")
    else:
        await message.answer(text, parse_mode="Markdown")

# هذا الهاندلر إضافي (اختياري) يستجيب لأمر /dev للتأكد من أن الروتر يعمل
@router.message(Command("dev"))
async def dev_command_test(message: Message):
    await message.answer("✅ روتر المطور يعمل بنجاح!")
