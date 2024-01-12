

from aiogram import  Router, types
from aiogram.types import Message
from aiogram.filters import Command
from keyboard import buttons1


router = Router()
user_baskets = {}

@router.message(Command("start"))
async def start_handler(msg: Message):
    user_id=msg.from_user.id
    name = msg.from_user.first_name
    print(name)
    if user_id not in  user_baskets:
        user_baskets[user_id] = []
    keyboard1 = types.InlineKeyboardMarkup(inline_keyboard=buttons1,resize_keyboard=True,)
    await msg.answer(f"ID{user_id}\n\nДоброго дня {name} ми продаємо телефони відомих брендів \n\n орентуйтися по меню щоб заказати телефон. ", reply_markup=keyboard1)
  
