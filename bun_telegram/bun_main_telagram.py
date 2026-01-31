from aiogram import Bot, Dispatcher, types

API_TOKEN = "7306565104:AAF__AsqxNnCemEQg7TSSjCf0vbz1yrT3U4"

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Меню магазина
menu = {
    "🍕 Pizza": 500,
    "🍔 Burger": 300,
    "🌭 Hot-dog": 200,
    "🥤 Ichimlik": 150
}

# Корзины пользователей
user_cart = {}

def food_keyboard():
    keyboard = [[types.KeyboardButton(text=item)] for item in menu]
    keyboard.append([
        types.KeyboardButton(text="🛒 Savatcha"),
        types.KeyboardButton(text="✅ Zakazni qabul qilish")
    ])
    return types.ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )

@dp.message(CommandStart())
async def start(message: types.Message):
    user_cart[message.from_user.id] = []
    await message.answer(
        "👋 Xush kelibsiz bun_magazin_bot ga!\nTaomni tangalang!:",
        reply_markup=food_keyboard()
    )

@dp.message(lambda m: m.text in menu)
async def add_to_cart(message: types.Message):
    user_id = message.from_user.id
    item = message.text

    user_cart.setdefault(user_id, []).append(item)

    await message.answer(
        f"✅ {item} Savatchaga qoshildi\nNarx: {menu[item]} $"
    )

@dp.message(lambda m: m.text == "🛒 Savatcha")
async def show_cart(message: types.Message):
    cart = user_cart.get(message.from_user.id, [])

    if not cart:
        await message.answer("🛒 Savatcha Bosh")
        return

    total = sum(menu[item] for item in cart)
    text = "🛒 Sizning savatchangiz:\n"
    for item in cart:
        text += f"- {item} — {menu[item]} $\n"

    text += f"\n💰 Hisob: {total} $"
    await message.answer(text)

@dp.message(lambda m: m.text == "✅ Zakazni qabul qilish")
async def order(message: types.Message):
    if not user_cart.get(message.from_user.id):
        await message.answer("❌ Savatcha bo`sh")
        return

    user_cart[message.from_user.id] = []
    await message.answer(
        "🎉 Zakazingiz qubul qilindi!\nRahmat,yana kelib turing ❤️",
        reply_markup=food_keyboard()
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())