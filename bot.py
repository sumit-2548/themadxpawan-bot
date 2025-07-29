from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InputMediaPhoto,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
import os

TOKEN = "8171331380:AAEOxdrZANqNYWxd84xwZ7N088FVvNBkCJ8"

ASSETS = "assets"
IMAGES = {
    "welcome": f"{ASSETS}/welcome.png",
    "start": f"{ASSETS}/welcome_start.png",
    "class9": f"{ASSETS}/class9th.png",
    "class10": f"{ASSETS}/class10th.png",
    "class11": f"{ASSETS}/class11th.png",
}

CHANNEL_LINKS = {
    "class9": "https://t.me/nexttoper9thAarambh",
    "class10": "https://t.me/nexttoper10thAarambh",
    "class11": "https://t.me/nexttoperclass11th",
}


async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo=open(IMAGES["welcome"], "rb"),
        caption="🚀 *Welcome to TheMadXpawan Bot.*\nCommand `/start` to begin your journey.",
        parse_mode="Markdown"
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    keyboard = [
        [
            InlineKeyboardButton("📘 Class 9", callback_data="class9"),
            InlineKeyboardButton("📗 Class 10", callback_data="class10"),
            InlineKeyboardButton("📙 Class 11", callback_data="class11"),
        ]
    ]

    await context.bot.send_photo(
        chat_id=chat_id,
        photo=open(IMAGES["start"], "rb"),
        caption=(
            "🤖 *Dear Student,*\n"
            "Welcome to TheMadXpawan Bot. Choose your class to start your *Free Learning Journey*."
        ),
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown",
    )


async def class_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    class_key = query.data
    class_label = class_key.replace("class", "Class ")
    img = IMAGES[class_key]
    link = CHANNEL_LINKS[class_key]

    media = InputMediaPhoto(open(img, "rb"))
    await context.bot.edit_message_media(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        media=media,
    )

    await context.bot.edit_message_caption(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        caption=(
            f"🎉 *Thank you for using Our bot!*\n\n"
            f"This is your destination link. Join this channel for *{class_label}* 📚:\n👉 {link}\n\n"
            "🔥 _Is baar system faad denge!!_"
        ),
        parse_mode="Markdown",
    )


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", welcome))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(class_handler))

    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()