from telegram import Update
from telegram.ext import ContextTypes
import db, config

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    full_name = f"{user.first_name or ''} {user.last_name or ''}".strip()
    db.add_user(user.id, full_name)
    await update.message.reply_text("✅ خوش آمدید! شما ثبت شدید.")

async def admin_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id in config.ADMINS:
        count = db.count_users()
        await update.message.reply_text(f"🔒 پنل مدیریت
تعداد کاربران ثبت‌شده: {count}")
    else:
        await update.message.reply_text("⛔ شما ادمین نیستید.")

async def echo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📩 پیام شما دریافت شد. (این پاسخ پیش‌فرض است)")
