from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import sec
import logging
import ephem
from datetime import datetime


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO, 
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def check_constellation(bot, update):
    """Фнукция которая возвращает созведие в котором находится планета, на вход принимает два параметра экземпляр бота и сообщение которое в него пришло."""
    
    def planet_info(user_planet):
        """ Функция возвращает созвездие где находится планета в текущий момент времени.
        На вход ожидает имя планеты"""
        try:
            # C помощью встроенной функции getattr получаем значение атрибута  объекта user_planet.
            planet = getattr(ephem, user_planet)()
            planet.compute(datetime.now())
            return f'В данный момент {user_planet} находится в созвездии:\n {ephem.constellation(planet)}'      
        except AttributeError:
            return f'Я ничего не знаю о {user_planet}'

    # Сеохраняем в переменную планету о которой хочет узнать пользователь.
    user_request = update.message.text.split(" ")
    user_planet = user_request[1].capitalize()

    logging.info(f'На вход пришло: {user_request}. После преобразования получили: "{user_planet}"')
    
    response_result = planet_info(user_planet)
    update.message.reply_text(response_result)
        
def word_count(bot, update):
    """ Функция подсчитывающая количество слов в фразе полученой после комманды """
    try:
        symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','№', ',', '.', '/', '<', '>', '\\', 
        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '-', '~', '`', ':', ';']
        
        user_request = update.message.text.split(' ')
        if len(user_request) == 1:
            return f'После команды "/wordcount" Вы не написали ни одного слова. \n{user_request}, \n {len(user_request)}'
        user_text = user_request[1:]
        
        def del_empty_item_list(user_list):
            user_list = [x for x in user_list if x]
            return user_list
            
        def del_symbols(some_text):
            for symbol in symbols:
                some_text = some_text.replace(symbol, ' ')
            return some_text        

        def convert_text(user_text):
            """ Функция принимает а вход список для конвертирования в другой список для подсчета слов """
            
            user_text_str = ' '.join(user_text)
            user_text_str = del_symbols(user_text_str)
            user_text = user_text_str.split(' ')
            user_text = del_empty_item_list(user_text)
            if len(user_text) == 0:
                return f'В указаном тексте нет слов.'
            else:
                return f'Кол-во слов в веденном элементе: {len(user_text)} шт.\nВ подсчет попали следующие слова: \n%s ' % "\n".join(user_text)

        response_result = convert_text(user_text)
        update.message.reply_text(response_result)

    except AttributeError:
        return f'В сообщении нет слов.'

def full_moon(bot, update):
    """Функция возвращает дату ближайщего полнолуния относительно даты в формате YYYY-MM-DD, введеной пользователем."""
    def full_moon_getdate(user_date):
        """По полученой на вход дате получаем дату полнолуния"""
        try:
            full_moon_date = ephem.next_full_moon(user_date)
            return full_moon_date
        except AttributeError:
            return f'Пока не уверен в данном исключении.'
                

    try:
        user_request = update.message.text.split(" ")
        user_date = datetime.strptime(user_request[1], '%Y-%m-%d') 
        logging.info(f'На вход пришло: {user_request}. После преобразования получили: "{user_date}::{type(user_date)}"')
        response_result = f'Для "{user_date.strftime("%Y-%m-%d")}", ближайщая дата полнолуния: {full_moon_getdate(user_date)}'
        update.message.reply_text(response_result)
    except ValueError:
        update.message.reply_text(f'Дату нужно вводить в формате: YYYY-MM-DD.')


def talk_to_me(bot, update):
    """ Простая функция для эхо ответа и записи информации в лог."""
    #Эхоответ:
    user_response = (f'Привет {update.message.chat.first_name}! Ты написал "{update.message.text}".')
    #Логирование:
    logging.info('User: %s, Chat id: %s, Message: %s',
                update.message.chat.username,
                update.message.chat.id,
                update.message.text)
    update.message.reply_text(user_response)

def main():
    """Основная функиця, запускающая бота."""
    #Подключаемся к платформе telegram
    mybot = Updater(sec.key, request_kwargs=sec.PROXY)
    #Пишем информацию в лог.
    logging.info('Бот запускается.')

    #Диспетчер, объект для коммутации входяшего сообшения к подписчику.
    dp = mybot.dispatcher

    #Отслеживаем команды и пердаем их подписчику (вызов функции):
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", check_constellation))
    dp.add_handler(CommandHandler("wordcount", word_count))
    dp.add_handler(CommandHandler("next_full_moon", full_moon))

    #Отслеживаем сообщения, и делаем эхос помошью функции talk_to_me.
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    #Начинаем общение с платформой телеграм, для проверки наличия сообщений:
    mybot.start_polling()
    
    #Работать бесконечно (пока не остановим)
    mybot.idle()

if __name__ == "__main__":
    main()
