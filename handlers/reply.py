from aiogram import Router, F
from aiogram.types import Message

router = Router()

# يمكنك إضافة أي كلمة ورد تريده هنا
replies = {
    "هلا": "هلا بيك نورت المجموعه! 🌹",
    "شلونك": "بخير الحمدلله، أنت شلونك؟",
    "بوت": "نعم، أنا بوت الحماية، كيف يمكنني مساعدتك؟"
}

@router.message(F.text.in_(replies.keys()))
async def auto_reply(message: Message):
    # يقوم البوت بالرد على الرسالة
    await message.reply(replies[message.text])
