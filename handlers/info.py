from aiogram import Router, F
from aiogram.types import Message, InputFile
from aiogram.types.input_file import FSInputFile

router = Router()

@router.message(F.text == "ايدي")
async def get_user_info(message: Message):
    # نحدد المستخدم (الشخص الذي رد عليه أو المستخدم نفسه)
    user = message.reply_to_message.from_user if message.reply_to_message else message.from_user
    
    # جلب صور البروفايل
    photos = await message.bot.get_user_profile_photos(user_id=user.id, limit=1)
    
    info_text = (
        f"☆-user : @{user.username or 'لا يوجد'}\n"
        f"☆-id : {user.id}\n"
        f"☆-الاسم : {user.full_name}"
    )

    # إذا كانت لديه صورة، نرسلها مع النص
    if photos.total_count > 0:
        photo_id = photos.photos[0][-1].file_id
        await message.reply_photo(photo=photo_id, caption=info_text)
    else:
        # إذا لم تكن لديه صورة، نرسل النص فقط
        await message.reply(info_text)
