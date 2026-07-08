from aiogram import Router, F
from aiogram.types import Message
from database import set_dev_id, get_dev_id

router = Router()

# أمر عرض المطور
@router.message(F.text == "المطور")
async def show_dev(message: Message):
    dev_id = get_dev_id()
    if not dev_id:
        return await message.reply("⚠️ لم يتم تعيين مطور بعد.")
    
    await message.reply(f"👨‍💻 **المطور الحالي:** [اضغط هنا للتواصل](tg://user?id={dev_id})")

# أمر تغيير المطور (فقط لك بصفتك المطور الأساسي أو الأدمن)
@router.message(F.text.startswith("تغيير المطور "))
async def change_dev(message: Message):
    # هنا يمكنك إضافة شرط (مثل: إذا كان آيديك هو X فقط يمكنه التغيير)
    new_id = message.text.split(" ")[2]
    set_dev_id(new_id)
    await message.reply(f"✅ تم تغيير المطور بنجاح إلى: {new_id}")
