from aiogram import Router, types, F
from aiogram.types import Message

router = Router()

# نستخدم .contains لكي يستجيب البوت إذا أرسلت كلمة "المطور" فقط أو حتى جملة فيها الكلمة
@router.message(F.text.contains("المطور"))
async def dev_info(message: Message):
    user = message.from_user
    
    # محاولة جلب الصورة
    try:
        photos = await message.bot.get_user_profile_photos(user_id=user.id, limit=1)
        
        text = (
            f"👤 المطور: {user.full_name}\n"
            f"🆔 الآيدي: `{user.id}`\n"
            f"🏷 اليوزر: @{user.username if user.username else 'لا يوجد'}"
        )

        if photos.total_count > 0:
            photo_file_id = photos.photos[0][-1].file_id
            await message.answer_photo(photo=photo_file_id, caption=text, parse_mode="Markdown")
        else:
            await message.answer(text, parse_mode="Markdown")
            
    except Exception as e:
        await message.answer(f"حدث خطأ أثناء جلب المعلومات: {e}")
