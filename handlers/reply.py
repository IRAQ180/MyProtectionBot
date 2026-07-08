from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text.contains("بوت"))
async def reply_bot(message: Message):
    await message.reply("نعم، أنا بوت الحماية، كيف يمكنني مساعدتك؟")

@router.message(F.text.contains("السلام عليكم"))
async def reply_hello(message: Message):
    await message.reply("وعليكم السلام ورحمة الله وبركاته! نورت المجموعه 🌹")
