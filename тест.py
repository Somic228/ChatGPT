import os
import aiogram
import openai

# Установка ключа API OpenAI
openai.api_key = os.getenv("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")

# Инициализация бота
bot = aiogram.Bot(token="6265729216:AAExpuiaO7P97sQ7JhbwtEMrwL-Snpf92sg")
dp = aiogram.Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_message(message: aiogram.types.Message):
    await message.reply("Hello! I'm an AI assistant. How can I help you today?")

# Обработчик входящих сообщений
@dp.message_handler()
async def ai_assistant(message: aiogram.types.Message):
    # Создание запроса к OpenAI API
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: {}\nAI:".format(message.text),
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    
    # Извлечение ответа из полученного ответа API
    ai_response = response.choices[0].text.strip()
    
    # Отправка ответа пользователю
    await message.reply(ai_response)

# Запуск бота
if __name__ == '__main__':
    aiogram.executor.start_polling(dp)
