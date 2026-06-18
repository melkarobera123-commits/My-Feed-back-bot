# Your Bot Token
BOT_TOKEN = "YOUR_BOT_TOKEN"

# Your Telegram ID
OWNER_ID = YOUR_TELEGRAM_ID


async def receive_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = update.message.text

    feedback_text = f"""
📩 New Feedback

👤 Name: {user.first_name}
🔗 Username: @{user.username}

💬 Message:
{message}
"""

    # Send feedback to you
    await context.bot.send_message(
        chat_id=OWNER_ID,
        text=feedback_text
    )

    # Reply to user
    await update.message.reply_text(
        "✅ Thank you for your feedback!"
    )


# Create bot application
app = Application.builder().token(BOT_TOKEN).build()

# Listen for all text messages
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, receive_feedback)
)

# Start bot
print("Bot is running...")
app.run_polling()
