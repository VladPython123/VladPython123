from aiogram import  Router, types, F
from keyboard import buttons3

router = Router()
user_baskets = {}


@router.callback_query(F.data == "iPhone")    
async def send1(call: types.CallbackQuery ):    
        global  user_baskets
        user_id = call.from_user.id
        if user_id not in user_baskets:
                user_baskets[user_id] = {"iPhone": 0, "Galaxy": 0, "Redmi": 0, "POCO": 0, "HUAWEI": 0,"total": 0}
        user_baskets[user_id]["iPhone"] += 1
        user_baskets[user_id]["total"] += 1200
        await call.message.answer('Ви успішно додали товар до кошика')
             
@router.callback_query(F.data == "Galaxy")    
async def send1(call: types.CallbackQuery ):    
        global   user_baskets
        user_id = call.from_user.id
        if user_id not in user_baskets:
                user_baskets[user_id] = {"iPhone": 0, "Galaxy": 0, "Redmi": 0, "POCO": 0, "HUAWEI": 0,"total": 0}
        user_baskets[user_id]["Galaxy"] += 1
        user_baskets[user_id]["total"] += 1300
        await call.message.answer('Ви успішно додали товар до кошика')
           
@router.callback_query(F.data == "Redmi")    
async def send1(call: types.CallbackQuery ):    
        global  user_baskets 
        user_id = call.from_user.id
        if user_id not in user_baskets:
                user_baskets[user_id] = {"iPhone": 0, "Galaxy": 0, "Redmi": 0, "POCO": 0, "HUAWEI": 0,"total": 0}
        user_baskets[user_id]["Redmi"] += 1
        user_baskets[user_id]["total"] += 380
        await call.message.answer('Ви успішно додали товар до кошика')
                 
@router.callback_query(F.data == "POCO")    
async def send1(call: types.CallbackQuery ):    
        global  user_baskets
        user_id = call.from_user.id
        if user_id not in user_baskets:
                user_baskets[user_id] = {"iPhone": 0, "Galaxy": 0, "Redmi": 0, "POCO": 0, "HUAWEI": 0,"total": 0}
        user_baskets[user_id]["POCO"] += 1
        user_baskets[user_id]["total"] += 400
        await call.message.answer('Ви успішно додали товар до кошика')
               
@router.callback_query(F.data == "HUAWEI")    
async def send1(call: types.CallbackQuery ):    
        global  user_baskets
        user_id = call.from_user.id
        if user_id not in user_baskets:
                user_baskets[user_id] = {"iPhone": 0, "Galaxy": 0, "Redmi": 0, "POCO": 0, "HUAWEI": 0,"total": 0}
        user_baskets[user_id]["HUAWEI"] += 1
        user_baskets[user_id]["total"] += 480
        await call.message.answer('Ви успішно додали товар до кошика')
          
@router.callback_query(F.data == "g2")
async def send(call: types.CallbackQuery ):
        global  user_baskets , basket_content
        user_id = call.from_user.id
        if user_id not in user_baskets:
                await call.message.answer("Кошик порожній!")
                return
        keyboard3 = types.InlineKeyboardMarkup(inline_keyboard=buttons3,resize_keyboard=True,)
        #basket_content = "\n".join([f"{item}: {count}" for item, count in user_baskets[user_id].items()])
        basket_content = "\n".join([f"{item}: {count}" for item, count in user_baskets[user_id].items() if item != "total"])
        await call.message.answer(f"Кошик:\n\n{basket_content}\n\nВаш рахунок: {user_baskets[user_id]['total']}$", reply_markup=keyboard3)
            
@router.callback_query(F.data == "wе1")
async def send(call: types.CallbackQuery ):
    global user_baskets , user_id 
    user_id=call.from_user.id
    user_baskets[user_id]["total"] -=  user_baskets[user_id]["total"]
    user_baskets[user_id]["iPhone"] -= user_baskets[user_id]["iPhone"]
    user_baskets[user_id]["Galaxy"] -= user_baskets[user_id]["Galaxy"]
    user_baskets[user_id]["Redmi"] -= user_baskets[user_id]["Redmi"]
    user_baskets[user_id]["POCO"] -= user_baskets[user_id]["POCO"]
    user_baskets[user_id]["HUAWEI"] -= user_baskets[user_id]["HUAWEI"]
    await call.message.answer(f"Ваш рахунок був обнульваний: 0 $ ") 
