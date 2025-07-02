from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN, ADMINS
from handlers import start_handler, admin_handler, echo_handler
import db

async def on_startup(app):
    db.init_db()
    print("Bot is running...")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).post_init(on_startup).build()
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("admin", admin_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_handler))
    app.run_polling()

if __name__ == "__main__":
    main()
