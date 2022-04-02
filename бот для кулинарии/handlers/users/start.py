from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Text

from loader import dp
from keyboards.default.menu import menu


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("Выберитие меню", reply_markup=menu)


@dp.message_handler(Text("🔍Поиск"))
async def bot_search(message: types.Message):
    await message.answer(
        "<i>✔️ Введите название блюда или категерию.</i>\n\n"

        "<b>✅ Правильно:</b> <i>Салат</i>\n"
        "<b>✅ Правильно:</b> <i>Оливье</i>\n\n"

        "<b>Жду от тебя названия блюда</b>👇\n"
        "<i>Приятного аппетита!</i>\n"
    )


@dp.message_handler(Text("🗃Категории"))
async def bot_search(message: types.Message):
    await message.answer("<b>Выберите кухню или нажмите на кнопку:</b> \"любая кухня\"")


@dp.message_handler(Text("⭐️Закладки"))
async def bot_search(message: types.Message):
    await message.answer("У вас нет закладок")


@dp.message_handler(Text("💥Популярное"))
async def bot_search(message: types.Message):
    await message.answer("<i>Самые популярные рецепты<i> 👇")


@dp.message_handler(Text("🍱Подбор по ингредиентам"))
async def bot_search(message: types.Message):
    await message.answer()


@dp.message_handler(Text("⚙️ Настройки"))
async def bot_search(message: types.Message):
    await message.answer("⚙️Настройки")


@dp.message_handler(Text("👥 Партнерка"))
async def bot_search(message: types.Message):
    await message.answer( 
        "<b>👥 Партнерская программа:</b> 0.2 руб. за реферала\n\n"

        "<b>🏆 Приглашено пользователей:</b> 0\n"  
        "<b>💰 Заработано всего:</b> 0 руб.\n"
        "<b>💳 Доступно на вывод:</b> 0 руб.\n\n"

        "<i>* для вывода обращайтесь в тех поддержку</i>\n\n"

        "Ваша партнерская ссылка:\n"
    )
