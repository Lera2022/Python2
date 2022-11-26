# python-telegram-bot   20.0a4
# запускается с /menu

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from content import *
import random

text_message = None


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def today(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    i = random.randint(0, 2)
    text_message = horoscopes[i]
    await update.message.reply_text(f'{update.effective_user.first_name}, \n{text_message}')


async def tomorrow(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    i = random.randint(0, 2)
    text_message = horoscopes[i]
    await update.message.reply_text(f'{update.effective_user.first_name}, \n{text_message}')


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Добро пожаловать в наш гороскоп:\n/today\n/tomorrow\n/my')


async def my(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Выберите ваш знак и напишите его название в ответ:\n♈ Овен\n♉ Телец\n♊ Близнецы\n♋ Рак\n♌ Лев\n♍ Дева\n♎ Весы\n♏ Скорпион\n♐ Стрелец\n♑ Козерог\n♒ Водолей\n♓ Рыбы')


async def sign(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text
    if message.lower() in signs:
        i = random.randint(0, 2)
        text_message = horoscopes[i]
    else:
        text_message = 'У нас пока ещё нет такого знака зодиака('
    await update.message.reply_text(f'{update.effective_user.first_name}, \n{text_message}')


app = ApplicationBuilder().token(
    "XXX").build()  # token

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("tomorrow", tomorrow))
app.add_handler(CommandHandler("today", today))
app.add_handler(CommandHandler("my", my))
app.add_handler(MessageHandler(filters.TEXT, sign))
app.run_polling()
