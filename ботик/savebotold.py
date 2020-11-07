import telebot
from telebot import types
import time
from bottle import run, post
bot = telebot.TeleBot('901945986:AAHBuiG4IrYSzStp9lHhVhmPBZNpVI-GoAk')
userStep = {}
chatgroup='-1001211184154'
v1='0'
v2='0'
v3='0'
v4='0'
v5='0'
v6='0'
v7='0'
def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:

        userStep[uid] = -1

        return 0
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Хочу помочь')
keyboard1.row('Юридическая консультация')
keyboard1.row('Признаки рабства')
keyboard1.row('Анализ')
keyboard1.row('О проекте')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('Исковое заявление')
keyboard2.row('Правовое обоснование')
keyboard2.row('Порядок обращения')
keyboard2.row('Назад')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('Да', 'Не знаю','Нет' )
keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard4.row('Узбекистан', 'Кыргызстан' )
keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard5.row('До 18', '18-50','50+','Не знаю' )
keyboard6 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard6.row('Мужской', 'Женский','Не знаю' )
keyboard7 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard7.row('Принудительный труд')
keyboard7.row('Cексуальное рабство')
keyboard7.row('не знаю')
keyboard8 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard8.row('Конвенция о рабстве 1926')
keyboard8.row('Конституция РК  от 30 августа 1995 года')
keyboard8.row('Международный пакт о гражданских и политических правах 1966')
keyboard8.row('Дополнительная Конвенция об упразднении рабства, работорговли и институтов и обычаев, сходных с рабством 1956г')
keyboard8.row('Всеобщая Декларация прав человека 1948г')
keyboard8.row('Международный пакт об экономических, социальных и культурных правах 1966г')
keyboard8.row('Гражданский кодекс Республики Казахстан (Общая часть), принят Верховным Советом Республики Казахстан 27 декабря 1994 года (с изменениями и дополнениями по состоянию на 10.01.2020 г.)')
keyboard8.row('Конвенция об упразднении принудительного труда 1957 года ')
keyboard8.row('Международная конвенция о защите всех прав трудящихся-мигрантов и членов их семей')
keyboard8.row('Конвенция Международная Организация Труда № 105 «Об упразднении принудительного труда')
keyboard8.row('Конвенция о запрещении и немедленных мерах по искоренению наихудших форм детского труда ')
keyboard8.row('Конвенция о правах инвалидов 2006')
keyboard8.row('Сиракузские принципы толкования ограничений и отступлений от положений Международного пакта о гражданских и политических правах')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, ' Здравствуйте!')
    bot.send_message(message.chat.id, ' Это телеграм бот для помощи людям в рабстве')
    bot.send_message(message.chat.id, "Выберите из списка", reply_markup=keyboard1)

@bot.message_handler(func=lambda message: message.text == "Хочу помочь")
def first_question(message):
    bot.send_message(message.chat.id,'Сколько лет пострадавшему?',reply_markup=keyboard5)
    userStep[message.chat.id] = 1


@bot.message_handler(func=lambda message: message.text == "Юридическая консультация")

def second_question(message):
    bot.send_message(message.chat.id, 'Выберите один из вариантов',reply_markup=keyboard2)
    userStep[message.chat.id] = 11

@bot.message_handler(func=lambda message: message.text == "Признаки рабства")

def third_question(message):
    with open("признаки рабства.png", "rb") as file:
        data = file.read()
        bot.send_photo(message.from_user.id, photo=data,reply_markup=keyboard1)
@bot.message_handler(func=lambda message: message.text == "Анализ")
def chet_question(message):
    doc = open('анализ_проблемы_торговли_людьми.pdf', 'rb')
    bot.send_document(message.chat.id, doc)
    bot.send_message(message.chat.id,'Выберите один из вариантов',reply_markup=keyboard1)
@bot.message_handler(func=lambda message: message.text == "О проекте")

def chet_question(message):
    bot.send_message(message.chat.id, 'Данный проект создан для помощи людям попавшим в рабство',reply_markup=keyboard1)

#Это все для первого вопроса
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 1)
def situation_1(message):
    global v1
    bot.send_message(message.chat.id, 'Какой пол пострадавшего?',reply_markup=keyboard6)
    v1=message.text
    userStep[message.chat.id] = 2
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 2)
def situation_2(message):
    global v2
    bot.send_message(message.chat.id, 'С какой целью удерживают жертву?',reply_markup=keyboard7)
    userStep[message.chat.id] = 3
    v2=message.text
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 3)
def situation_3(message):
    global v3
    v3=message.text
    bot.send_message(message.chat.id, 'Ваш номер для контакта')
    userStep[message.chat.id] = 4
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 4)
def situation_3(message):
    global v4
    v4=message.text
    bot.send_message(message.chat.id, 'Напишите местоположение жертвы(Ecли неизвестно напишите "нет")')
    userStep[message.chat.id] = 5
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 5)
def situation_3(message):
    global v5
    v5=message.text
    bot.send_message(message.chat.id, 'Жертва гражданин рк?',reply_markup=keyboard3)
    userStep[message.chat.id] = 6
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 6)
def situation_4(message):
    global v6
    v6=message.text
    if message.text=="Да":
        userStep[message.chat.id] = 5

        with open("1.png", "rb") as file:
            data = file.read()
            bot.send_photo(message.from_user.id, photo=data)
        time.sleep(2)
        bot.send_message(message.chat.id, 'Мы записали ваш ответ',reply_markup=keyboard1)
        bot.send_message(chatgroup, v1+'\n '+v2+' \n'+v3+'\n '+v4+'\n '+v5+'\n '+v6+'\n '+v7,reply_markup=keyboard1)
    if message.text=='Не знаю':
        userStep[message.chat.id] = 5
        with open("2.png", "rb") as file:
            data = file.read()
            bot.send_photo(message.from_user.id, photo=data)
        time.sleep(2)
        bot.send_message(message.chat.id, 'Мы записали ваш ответ',reply_markup=keyboard1)
        bot.send_message(chatgroup, v1+'\n '+v2+' \n'+v3+'\n '+v4+'\n '+v5+'\n '+v6+'\n '+v7,reply_markup=keyboard1)
    if message.text=='Нет':
        userStep[message.chat.id] = 7
        bot.send_message(message.chat.id, 'Какая страна?',reply_markup=keyboard4)
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 7)
def situation_5(message):
    global v7
    v7=message.text
    if message.text=="Кыргызстан":
        userStep[message.chat.id] = 5
        with open("kg.png", "rb") as file:
            data = file.read()
            bot.send_photo(message.from_user.id, photo=data)
        time.sleep(2)
        bot.send_message(message.chat.id, 'Мы записали ваш ответ',reply_markup=keyboard1)
        bot.send_message(chatgroup, v1+'\n '+v2+' \n'+v3+'\n '+v4+'\n '+v5+'\n '+v6+'\n '+v7,reply_markup=keyboard1)
    if message.text=='Узбекистан':
        userStep[message.chat.id] = 5
        with open("uz.png", "rb") as file:
            data = file.read()
            bot.send_photo(message.from_user.id, photo=data)
        time.sleep(2)
        bot.send_message(message.chat.id, 'Мы записали ваш ответ',reply_markup=keyboard1)
        bot.send_message(chatgroup, v1+'\n '+v2+' \n'+v3+'\n '+v4+'\n '+v5+'\n '+v6+'\n '+v7,reply_markup=keyboard1)

#Это все для второго вопроса
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 11)
def situation_4(message):
    if message.text=="Исковое заявление":
        doc = open('иск моральный вред.docx', 'rb')
        bot.send_document(message.chat.id, doc)
        bot.send_message(message.chat.id,'Выберите один из вариантов',reply_markup=keyboard2)
    if message.text=='Правовое обоснование':
        bot.send_message(message.chat.id,'Заявляем письменно В случае, когда необходимо сообщить об уже произошедшем или готовящемся правонарушении, следует прийти в любое отделение полиции и заявить об этом. Заявления об уголовных правонарушениях принимаются сотрудниками полиции в установленной форме. Образцы заявлений вам предоставят в отделении. В случае, если имеются документы, подтверждающие факт правонарушения, они должны быть вами приобщены к поданному заявлению. Внимание! На письменное заявление в полиции вам в обязательном порядке должны выдать талон-уведомление. Именно этот документ подтверждает факт обращения в полицию. Когда вам могут отказать Вместе с тем, практика показывает, что значительное количество заявлений оказываются в дальнейшем без досудебного расследования, дела по ним полиция не возбуждает. Главным образом это происходит потому, что с юридической точки зрения в таких заявлениях отсутствуют признаки уголовного правонарушения. К примеру, при подаче заявления об утере имущества (мобильного телефона, кошелька, документов и пр.), при отсутствии в нем явных признаков совершения хищения, обращения граждан, как правило, списываются в номенклатурное дело и остаются без рассмотрения. Другой наиболее распространенный пример – списание сообщений без их рассмотрения по делам частно-публичного характера. К ним относятся такие распространенные статьи Уголовного Кодекса, как мошенничество (ст.190 ч.1 УК РК), изнасилование (ст.120 ч.1 УК РК) и другие. По указанным статьям сотрудниками правоохранительных органов заведение досудебных производств не может быть начато не иначе как по жалобе непосредственно потерпевших.',reply_markup=keyboard8)
    if message.text=='Порядок обращения':
        with open("ПРОЕКТ 128 СХЕМА ОБР.png", "rb") as file:
            data = file.read()
            bot.send_photo(message.from_user.id, photo=data)
        bot.send_message(message.chat.id,'Свидетель, жертва, очевидец Если каким-то образом вы стали очевидцем, свидетелем нарушения закона, или сами стали жертвой преступных посягательств, вам необходимо обратиться в полицию. Сотрудники органов внутренних дел должны оперативно отреагировать на поступивший сигнал, установить виновных лиц, принять меры по привлечению их к ответственности. Однако, и это признают даже в прокуратуре, в этой на первый взгляд простой схеме нередко возникают сложности. Вот наиболее типичные из них. Устное заявление Случаются ситуации, когда правонарушение произошло на ваших глазах и оперативность обращения в полицию поможет быстрее раскрыть его. Например, вы видите происходящую драку, ограбление, кражу. В данном случае, эффективнее как можно быстрее устно проинформировать об этом сотрудников полиции по телефону 102. При этом необходимо помнить, что анонимное сообщение не может являться основанием для уголовного разбирательства. Однако и оно обязательно будет зарегистрировано и рассмотрено в установленном порядке. Звонки граждан, поступающие на номер 102, записываются и в дальнейшем перепроверяются должностными лицами МВД и прокуратуры. Поэтому не сообщайте заведомо ложные сведения, в том числе о себе, так как за это в дальнейшем вы можете понести ответственность. В целом ваша конфиденциальность будет сохранена. Даже если в дальнейшем от вас потребуется выступление в суде в качестве свидетеля, то и здесь ваше инкогнито будет полностью сохранено. Для этого у органов следствия и суда в настоящее время имеется достаточно механизмов. Стоит конечно помнить, что помощь следствию и суду является не только правом, но и обязанностью законопослушного гражданина Республики Казахстан. И уклонение от нее также чревато ответственностью.',reply_markup=keyboard2)
    if message.text=='Назад':
        userStep[message.chat.id] = 0
        bot.send_message(message.chat.id,'Первое меню',reply_markup=keyboard1)


bot.polling()
