from aiogram import Router, F
from aiogram.types import Message
from database import get_reply

router = Router()

@router.message(F.text)
async def auto_reply(message: Message):
    # جلب الرد من قاعدة البيانات
    reply_text = get_reply(message.text)
    
    # إذا وجدنا رداً في القاعدة، قم بالرد
    if reply_text:
        await message.reply(reply_text)
