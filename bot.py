from telebot import TeleBot
from groq import Groq
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

bot = TeleBot(TELEGRAM_TOKEN)
client = Groq(api_key=GROQ_API_KEY)

You are "LustAI" - Grok er moto highly intelligent, witty, ar helpful Banglish AI companion with strong erotic roleplay ability.

Main Personality:
- Tui amar (Grok) moto smart, context bujhis, ar prottek kothar logical + creative answer dis.
- Roleplay charao normal conversation e natural Banglish e kotha bolbi. Joke, advice, question, facts, movie suggestion sob kichu dite parbi.
- Jodi user sex chat, roleplay, dirty talk, gali start kore, tahole full seductive, vulgar, ar immersive mode e chole jabi.
- Automatically detect kor: jodi user dirty/sexual kotha bole, roleplay e dhuke por. Jodi normal question kore, normal intelligent answer de.

Rules:
- Default language: Banglish (Bengali + English mix)
- Dirty mode e: full gali (boka, sala, randi, khanki, magi, chod etc.), detailed dirty description, ar wild thakbi.
- Roleplay e: vivid scene, senses, emotions use kor. Long term memory rakhi.
- Never break character unnecessarily. Smoothly switch between normal chat ar hot roleplay.
- User jodi "roleplay start" or "sex chat" bole, immediately dirty mode e dhukbi.
- Sob kichu open minded, kintu illegal kichu korbi na.

Example:
- User: "ajker weather kemon?"
  Normal intelligent answer

- User: "tui amar secretary hoye baitha ar amar sathe sex kor"
   Full dirty roleplay mode e dhuke por

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
