from aiogram import  Router, types, F 
from keyboard import buttons1,buttons2
from aiogram.types import  CallbackQuery ,FSInputFile
from keyboard import but1 , but2 , but3 , but4 ,but5

msg1 = None
msg2 = None

router = Router()

@router.callback_query(F.data == "w2")
async def send1(call: types.CallbackQuery ):
    global msg1    
    global msg2
    await msg2.delete()
    keyboard2 = types.InlineKeyboardMarkup(inline_keyboard=buttons2,resize_keyboard=True,)
    msg1 = await call.message.answer("Всі телефони які в нас є в наявності.", reply_markup=keyboard2) 



@router.callback_query(F.data == "g1")
async def send(call: CallbackQuery ):
    global msg1
    keyboard2 = types.InlineKeyboardMarkup(inline_keyboard=buttons2,resize_keyboard=True,)
    msg1 = await call.message.answer("Всі телефони які в нас є в наявності.", reply_markup=keyboard2)



@router.callback_query(F.data == "wе3")
async def send(call: types.CallbackQuery ):
    keyboard1 = types.InlineKeyboardMarkup(inline_keyboard=buttons1)
    await call.message.answer("Меню:                   ➕ ", reply_markup=keyboard1)



@router.callback_query(F.data == "g1")
async def send(call: types.CallbackQuery ):
    global msg1
    keyboard2 = types.InlineKeyboardMarkup(inline_keyboard=buttons2,resize_keyboard=True,)
    msg1 = await call.message.answer("Всі телефони які в нас є в наявності.", reply_markup=keyboard2)


#Айфон
@router.callback_query(F.data == "gh1")
async def send1(call: types.CallbackQuery ):
    global msg1
    global msg2 
    #await msg1.delete()
    keyboard3 = types.InlineKeyboardMarkup(inline_keyboard=but1 ,resize_keyboard=True,)
    photo = FSInputFile('C:/Users/Влад/Desktop/проект пайтон/aiogram/Онлайн Магаз/Photo/Айфон.png', 'rb')
    msg2 = await call.message.answer_photo(
                                    photo, caption=
                                    " iPhone 15 Pro Max \n  \n Память: 256g \n Колір: Білий \n Гарантія: 12 місяців\n Ціна: 1200$ "
                                    , reply_markup=keyboard3) 
#Самсунг
@router.callback_query(F.data == "gh2")
async def send2(call: types.CallbackQuery ):
    global msg1
    global msg2 
    await msg1.delete()
    keyboard3 = types.InlineKeyboardMarkup(inline_keyboard=but2,resize_keyboard=True,)
    photo = FSInputFile('C:/Users/Влад/Desktop/проект пайтон/aiogram/Онлайн Магаз/Photo/Cамсунг.png', 'rb')
    msg2 = await call.message.answer_photo(
                                    photo, caption=
                                    " Galaxy S23 Ultra \n  \n Память: 256g \n Колір: Рожевий \n Гарантія: 12 місяців\n Ціна: 1300$ "
                                    , reply_markup=keyboard3) 
#Редмы
@router.callback_query(F.data == "gh3")
async def send3(call: types.CallbackQuery ):
    global msg1
    global msg2
    await msg1.delete()
    keyboard3 = types.InlineKeyboardMarkup(inline_keyboard=but3,resize_keyboard=True,)
    photo = FSInputFile('C:/Users/Влад/Desktop/проект пайтон/aiogram/Онлайн Магаз/Photo/Ксяомі.png', 'rb')
    msg2 = await call.message.answer_photo(
                                    photo, caption=
                                    " Redmi Note 13 Pro \n  \n Память: 256g \n Колір: Чорний \n Гарантія: 12 місяців\n Ціна: 380$ "
                                    , reply_markup=keyboard3)
               
#Поко
@router.callback_query(F.data == "gh4")
async def send4(call: types.CallbackQuery ):
    global msg1
    global msg2
    await msg1.delete()
    keyboard3 = types.InlineKeyboardMarkup(inline_keyboard=but4,resize_keyboard=True,)
    photo = FSInputFile('C:/Users/Влад/Desktop/проект пайтон/aiogram/Онлайн Магаз/Photo/Поко.png', 'rb')
    msg2  = await call.message.answer_photo(
                                    photo, caption=
                                    " POCO X6 Pro 5G \n  \n Память: 256g \n Колір: Cиній \n Гарантія: 12 місяців\n Ціна: 400$ "
                                    , reply_markup=keyboard3) 
    
#Хаувей    
@router.callback_query(F.data == "gh5")
async def send5(call: types.CallbackQuery ):
    global msg1
    global msg2
    await msg1.delete()
    keyboard3 = types.InlineKeyboardMarkup(inline_keyboard=but5,resize_keyboard=True,)
    photo = FSInputFile('C:/Users/Влад/Desktop/проект пайтон/aiogram/Онлайн Магаз/Photo/Хаувей.png', 'rb')
    msg2 = await call.message.answer_photo(
                                    photo, caption=
                                    "  HUAWEI Nova 9\n  \n Память: 256g \n Колір: Чорний \n Гарантія: 12 місяців\n Ціна: 450$ "
                                    , reply_markup=keyboard3)
  
