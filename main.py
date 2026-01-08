import telebot
import random

# Apna API Token yahan dalein
API_TOKEN = '8322362394:AAF4otIG8AE9QXYk-weY4cbNVOgd4ESsWbE'
bot = telebot.TeleBot(API_TOKEN)

def get_prediction():
    # Ye logic pattern base par hai
    # 0-4: Small, 5-9: Big
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    colors = ["Red 🔴", "Green 🟢", "Violet 🟣"]
    
    predicted_num = random.choice(numbers)
    
    if predicted_num <= 4:
        size = "SMALL"
    else:
        size = "BIG"
        
    color = random.choice(colors)
    
    return f"✨ Prediction ✨\n\nNumber: {predicted_num}\nSize: {size}\nColor: {color}"

@bot.message_handler(commands=['start', 'predict'])
def predict_message(message):
    prediction_text = get_prediction()
    bot.reply_to(message, prediction_text)

print("Bot chal raha hai...")
bot.polling()
