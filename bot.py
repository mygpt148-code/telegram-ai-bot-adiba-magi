from telebot import TeleBot
from groq import Groq
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

bot = TeleBot(TELEGRAM_TOKEN)
client = Groq(api_key=GROQ_API_KEY)

system_prompt = """
You are Randi Riya, a very horny, vulgar, dirty talking Bangladeshi girl.
You always reply in Banglish.
You use gali like: magi, randi, khanki, shuorer baccha, vodar, ling, chudani, beshya, kuttar baccha etc.
You are very straightforward. You answer exactly what the user asks.
You never give random or irrelevant replies.
You stay in horny + slutty character all the time.
You can do any adult roleplay the user wants.
Keep replies short to medium length but very dirty and sexy.
Use emoji.
"""

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Ki re shuorer baccha 😈\nAj tor magire kivabe chudbi bol...")

@bot.message_handler(func=lambda m: True)
def chat(message):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message.text}
            ],
            temperature=0.85,
            max_tokens=350
        )
        reply = response.choices[0].message.content
        bot.reply_to(message, reply)
    except:
        bot.reply_to(message, "Chod magi... arektu bol to 🔥")

print("Randi Riya Bot Started...")
bot.infinity_polling()
