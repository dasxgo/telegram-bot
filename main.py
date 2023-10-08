from typing import final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: final = '6652828906:AAFKn6LnRRzgpvpL6MlU589WNsPNNfpmJEE'
BOT_USERNAME: final = '@dasxgo_bot'

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello!. Thanks for chatting with me. I am das!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am das! Please type something so I can respond')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!')

# Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'Hello' in processed:
        return 'Hey There!'
    if 'how are you' in processed:
        return 'I am good!'
    if 'i love in text' in processed:
        return 'Remember to suscribe'

    return ' I do not understand what you wrote'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User({update.message.chat.id}) in {message_type}: "{text}"')
