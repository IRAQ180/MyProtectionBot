from aiogram import Router, F
from aiogram.types import Message
from database import set_rank, remove_rank, get_rank, get_rank_level

router = Router()

# أمر رفع رتبة
@router.message(F.text.startswith("رفع "))
async def promote_user(message: Message):
    if not message.reply_to_message:
        return await message.reply("⚠️ يرجى الرد على رسالة العضو لرفعه.")
    
    # تقسيم الأمر (مثال: رفع ادمن)
    parts = message.text.split(" ", 1)
    if len(parts) < 2:
        return await message.reply("⚠️ صيغة خاطئة! استخدم: رفع [الرتبة]")
    
    target_id = message.reply_to_message.from_user.id
    new_rank = parts[1]
    
    set_rank(target_id, new_rank)
    await message.reply(f"✅ تم رفع العضو إلى رتبة: {new_rank}")

# أمر تنزيل رتبة
@router.message(F.text == "تنزيل")
async def demote_user(message: Message):
    if not message.reply_to_message:
        return await message.reply("⚠️ يرجى الرد على رسالة العضو لتنزيله.")
    
    target_id = message.reply_to_message.from_user.id
    remove_rank(target_id)
    await message.reply("✅ تم تنزيل العضو من رتبته وأصبح (عضو).")

# أمر كشف الرتبة
@router.message(F.text == "رتبتي")
async def check_rank(message: Message):
    user_id = message.from_user.id
    rank = get_rank(user_id)
    await message.reply(f"👤 رتبتك الحالية هي: {rank}")
