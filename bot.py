from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "توکن رباتتو اینجا بذار"

# لیست قراردادهای رایگان
free_contracts = {
    "قرارداد جوشکاری اسکلت فلزی": "این قرارداد بین آقای ... و آقای ... جهت اجرای جوشکاری اسکلت فلزی منعقد می‌شود..."
}

# لیست قراردادهای پرداختی (در آینده می‌تونه پولی بشه)
paid_contracts = {
    "قرارداد مدیریت پیمان": "این قرارداد بین کارفرما و مدیر پیمان منعقد شده و شامل تعهدات اجرایی، مالی و نظارتی می‌باشد..."
}

# شروع ربات
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("قراردادهای رایگان", callback_data="free")],
        [InlineKeyboardButton("قراردادهای ویژه (پرداختی)", callback_data="paid")],
        [InlineKeyboardButton("درباره ما", callback_data="about")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("به ربات قراردادهای عمرانی خوش آمدید!", reply_markup=reply_markup)

# واکنش به دکمه‌ها
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "free":
        text = "قراردادهای رایگان:\n"
        for title in free_contracts:
            text += f"\n- {title}"
        await query.edit_message_text(text=text)

    elif query.data == "paid":
        text = "برای دریافت قراردادهای ویژه ابتدا باید پرداخت انجام دهید. در حال حاضر این بخش آماده‌سازی است."
        await query.edit_message_text(text=text)

    elif query.data == "about":
        await query.edit_message_text(text="این ربات توسط ساسان بابان برای ارائه قراردادهای تخصصی عمران ساخته شده است.")

# اجرای ربات
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()
