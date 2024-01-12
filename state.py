from aiogram.fsm.state import StatesGroup , State
from aiogram.fsm.context import FSMContext
from aiogram import F, types, Router
from aiogram.types import CallbackQuery
from keyboard import buttons4

router = Router() 

name  = ''
num = ''
region = ''

class Form (StatesGroup):
    r1= State()
    r2 = State()
    r3 = State()
    
  
    
@router.callback_query(F.data == "wе2" )
async def zakaz(call: CallbackQuery , state: FSMContext):
    await state.set_state(Form.r1)
    await call.message.answer("Введіть своє імя:") 
    
@router.message(Form.r1)
async def zakaz(msg: types.Message, state: FSMContext):
    global name
    name = msg.text.strip()
    await state.set_state(Form.r2)
    await msg.answer("Введіть свій номер телефону ")
   
    
@router.message(Form.r2)
async def message(msg: types.Message,state: FSMContext):
    if msg.text.isdigit:
        global num
        num = msg.text.strip()
        await msg.answer("Введіть де ви проживаєте ")
        await state.set_state(Form.r3)
    else:
        await msg.answer("Вветь числами !!!")
            
    
@router.message(Form.r3)
async def msg(msg: types.Message):
    global name
    global num
    global region
    region = msg.text.strip()
    keyboard4 = types.InlineKeyboardMarkup(inline_keyboard=buttons4,resize_keyboard=True,)
    await msg.answer(f"Ім'я: {name} \n Номер: {num} \n Регіон: {region} ",reply_markup=keyboard4)
    
    
@router.callback_query(F.data == "wz1" )
async def zakaz2(call: CallbackQuery , state: FSMContext):
    await state.set_state(Form.r1)
    await call.message.answer("Введіть своє імя:")  
 
    
@router.callback_query(F.data == "wz2")
async def zakaz(call: CallbackQuery ):
    await call.answer(text="Вітаю ваший заказ був прийнятий🎉",show_alert=True)
    await call.message.answer("Вітаю ваз заказ прийнятий !!!!") 
