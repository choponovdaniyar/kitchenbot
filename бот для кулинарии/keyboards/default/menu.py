from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButton



menu=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="🔍Поиск",
            ),
            KeyboardButton(
                text="🗃Категории",
            ),
        ],
        [
            KeyboardButton(
                text="⭐️Закладки",
            ),
            KeyboardButton(
                text="💥Популярное",
            ),
        ],
        [
            KeyboardButton(
                text="🍱Подбор по ингредиентам",
            )
        ],
        [
            KeyboardButton(
                text="⚙️ Настройки",
            ),
            KeyboardButton(
                text="👥 Партнерка",
            ),
        ],
    ]
)