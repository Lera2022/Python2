from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def goodbye(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Goodbye {update.effective_user.first_name}')

async def msg(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file_to_download = await update.message.document.get_file()

    file_path = await file_to_download.download()
    os.system(f'python {file_path} > {str(file_path)}.out 2> {str(file_path)}.error')
    text_message = None
    with open(str(file_path) + '.out') as f:
        text_message = f.read()

    if text_message == '':
        with open(str(file_path) + '.error') as f:
            text_message = f.read()
    
    if text_message == '':
        text_message = 'Nothing to output'
        
    await update.message.reply_text(text_message)

app = ApplicationBuilder().token("XXX").build() # token

app.add_handler(MessageHandler(filters.Document.FileExtension("py"), msg))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("goodbye", goodbye))


app.run_polling()