from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database import add_reply

router = Router()

# تعريف حالات الانتظار
class AddReplyStates(StatesGroup):
    waiting_for_key = State()
    waiting_for_value = State()

# الخطوة 1: المستخدم يكتب "اضف رد"
@router.message(F.text == "اضف رد")
async def start_add_reply(message: Message, state: FSMContext):
    await message.reply("أهلاً بك! ما هي الكلمة التي تريدني أن أرد عليها؟")
    await state.set_state(AddReplyStates.waiting_for_key)

# الخطوة 2: البوت ينتظر الكلمة
@router.message(AddReplyStates.waiting_for_key)
async def get_key(message: Message, state: FSMContext):
    await state.update_data(key=message.text)
    await message.reply("تم حفظ الكلمة. الآن، ماذا تريد أن يكون ردي عليها؟")
    await state.set_state(AddReplyStates.waiting_for_value)

# الخطوة 3: البوت ينتظر الرد ويحفظه في القاعدة
@router.message(AddReplyStates.waiting_for_value)
async def get_value(message: Message, state: FSMContext):
    data = await state.get_data()
    key = data['key']
    value = message.text
    
    add_reply(key, value) # حفظ في القاعدة
    await message.reply(f"✅ تم الحفظ بنجاح!\nالكلمة: {key}\nالرد: {value}")
    await state.clear() # إنهاء الحالة والعودة للوضع الطبيعي
