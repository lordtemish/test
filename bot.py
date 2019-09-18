import config
import time
import telebot
from telebot import types

won=0
num=35
users=dict()
winner=""

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    s=message.text
    keyboard = types.InlineKeyboardMarkup()
    global won
    global users
    global winner
    accept=True
    answer=''

    cid=message.chat.id
    user=message.from_user.username
    print(users)
    now=time.time()
    if(user not in users):
        users[user]=now
    else:
    
        old=users[user] 
        if(now-old<5):
            accept=False
        else:
            users[user]=now
        print(old, now, old-now)

    if(user==None):
        accept=False

    if(accept):
        if(s.lower()=='привет'):
            answer='Привет'
        elif(s.lower()=='мяу'):
            answer="Бля, хочу внюхаться пиздец"
        elif(s.lower()=='плуг'):
            answer="LOLA + PLUG 4EVER"
        elif('иди на хуй' in s.lower()):
            answer="На хуй не идут на хуй ложаться"
        elif('lola' in s.lower()):
            answer="Ау жаным?"
        elif("лола" in s.lower()):
            answer="Я - Лола, я ахуенна, а ты хуйло ебаное, не пиши сюда больше, понял?"
        elif ("да"==s.lower()):
            answer="Хуй на, котагынды жеме"
        elif("нет"==s.lower() ):
            answer="Пидора ответ, а ты пидор в колготках вот тебе и похуй"
        elif("как дела" in s.lower()):
            answer='У меня все хорошо, у тебя как?'
        elif(s.lower() == '/start'):
            answer='А ты знаешь что я самая ахуенная?';
            callback_button = types.InlineKeyboardButton(text="Кто самая пиздатая баба?", callback_data="test")
            keyboard.add(callback_button)
        elif(s.lower() == 'салам'):
            answer='Алейкум нахой, далбаёб!'
        elif('чё' in s.lower() or 'че' in s.lower()):
            answer="Ашалам нахуй!!! "
        elif("го ебаться" in s.lower() or "го ебатся" in s.lower() or "го ебаца" in s.lower()):
            answer="Снимай трусы, страпон готов! ИХИХИХИХ"
        elif(str(num)==s):
            if(checkW()):
                answer="Ответ правильный, но победитель уже найден"
            else:
                winner=user
                won+=1
                answer="Ура вы победитель пишите к @fuckthe12 или кидайте в НПА скрин \n WINNER : "+winner
                print(user,"won")
        elif("check" in s.lower()):
            if(checkW()):
                answer="Победитель найден"+" @"+winner
            else:
                answer="Победитель еще не найден"
        else:
            answer='Игнорирую всяких пидарасов, особенно если не понимаю'
    else:
        if(user==None):
            answer="У вас нет юзернейма создайте юзернейм"
        else:
            answer="Вы отправляете сообщения слишком часто, ждите несколько секунд"

    bot.send_message(message.chat.id, answer, reply_markup=keyboard)

def checkW():
    return won==1
def setWin():
    won=1

@bot.inline_handler(lambda query: len(query.query) > 0)
def query_text(query):
    kb = types.InlineKeyboardMarkup()
    # Добавляем колбэк-кнопку с содержимым "test"
    kb.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="test"))
    results = []
    single_msg = types.InlineQueryResultArticle(
        id="1", title="Press me",
        input_message_content=types.InputTextMessageContent(message_text="Я – сообщение из инлайн-режима"),
        reply_markup=kb
    )
    results.append(single_msg)
    bot.answer_inline_query(query.id, results)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "test":
            #bot.send_message(message.chat.id, "Лола Банни королева зиплоков, ну это все знают, а ты попробуй написать мне что-нибудь")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Лола Банни королева зиплоков, ну это все знают, а ты попробуй написать мне что-нибудь")
    # Если сообщение из инлайн-режима
    elif call.inline_message_id:
        if call.data == "test":
            #bot.send_message(message.chat.id, "Лола Банни королева зиплоков")
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="Лола Банни королева зиплоков, ну это все знают, а ты попробуй написать мне что-нибудь")


if __name__ == '__main__':
     bot.polling(none_stop=True)