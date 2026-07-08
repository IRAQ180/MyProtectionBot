from aiogram import Router, F
from aiogram.types import Message
from database import get_rank, get_rank_level

router = Router()

# أمر مسح الرسائل (تنظيف)
@router.message(F.text.startswith("مسح "))
async def clean_messages(message: Message):
    # التحقق من رتبة المستخدم (يجب أن يكون ادمن أو أعلى)
    user_rank = get_rank(message.from_user.id)
    if get_rank_level(user_rank) < 3:
        return await message.reply("⚠️ عذراً، هذا الأمر مخصص للادمن فما فوق.")

    # أخذ عدد الرسائل
    try:
        count = int(message.text.split(" ")[1])
    except:
        return await message.reply("⚠️ يرجى تحديد عدد الرسائل، مثال: مسح 10")

    # حذف الرسائل
    try:
        for i in range(count + 1): # +1 لحذف أمر المسح أيضاً
            await message.chat.delete_message(message.message_id - i)
    except Exception as e:
        await message.reply("⚠️ لا يمكنني حذف الرسائل، تأكد أنني مشرف في المجموعة.")

# أمر تنظيف البوت من الردود أو التنبيهات
@router.message(F.text == "تنظيف")
async def simple_clean(message: Message):
    await message.delete()
