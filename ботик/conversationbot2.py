

from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, PicklePersistence, CallbackQueryHandler)
from telegram import Document
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
v=0
v1='0'
v2='0'
v3='0'
v4='0'
v5='0'
v6='0'
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

CHOOSING, TYPING_CHOICE ,q1,q2,q3,q4,q5,q6 = range(8)

reply_keyboard = [['Хочу помочь', 'Юридическая консультация'],
                  ['Признаки рабства', 'Анализ проблеммы'],
                  ['О проекте']]
reply_keyboard2 = [['Исковое заявление',
    'Правовое обоснование'],
    ['Порядок обращения',
    'Назад']]
reply_keyboard3 =[['Да','Не знаю','Нет']]
reply_keyboard4 =[['Узбекистан', 'Кыргызстан' ]]
reply_keyboard5 =[['До 18', '18-50','50+','Не знаю' ]]
reply_keyboard6 =[['Мужской', 'Женский','Не знаю']]
reply_keyboard7 =[['Принудительный труд'],['Cексуальное рабство'],['Не знаю']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=True)
markup3 = ReplyKeyboardMarkup(reply_keyboard3, one_time_keyboard=True)
markup4 = ReplyKeyboardMarkup(reply_keyboard4, one_time_keyboard=True)
markup5 = ReplyKeyboardMarkup(reply_keyboard5, one_time_keyboard=True)
markup6 = ReplyKeyboardMarkup(reply_keyboard6, one_time_keyboard=True)
markup7 = ReplyKeyboardMarkup(reply_keyboard7, one_time_keyboard=True)

def facts_to_str(user_data):
    facts = list()

    for key, value in user_data.items():
        facts.append('{} - {}'.format(key, value))

    return "\n".join(facts).join(['\n', '\n'])


def start(update, context):
    update.message.reply_text(
        "Здравствуйте! Это телеграм бот для помощи людям в рабстве\n\n"
        "Выберите что вам нужно:",
        reply_markup=markup)

    return CHOOSING


def button(update, context):
    global v,v1,v2,v3,v4,v5,v6
    if update.message.text=='Хочу помочь':
        update.message.reply_text(text="Сколько лет пострадавшему? ",reply_markup=markup5)
        v1=update.message.text
        return q1
    if update.message.text=='18-50' or update.message.text=='До 18' or update.message.text=='50+' or update.message.text=='Не знаю':
        update.message.reply_text(text="Какой пол пострадавшего? ",reply_markup=markup6)
        v2=update.message.text
        return q2
    if update.message.text=='Мужской' or update.message.text=='Женский' or update.message.text=='Не знаю':
        update.message.reply_text(text="С какой целью удерживают жертву? ",reply_markup=markup7)
        v3=update.message.text
        return q3
    if update.message.text=='Принудительный труд'or update.message.text=='Cексуальное рабство' or update.message.text=='Не знаю':
        update.message.reply_text(text="Ваш номер для контакта ")
        v4=update.message.text
        v=5
        return q4
    if v==5:
        update.message.reply_text(text="Напишите местоположение жертвы(Ecли неизвестно напишите \"нет\") ")
        v=6
        v5=update.message.text
        return q5
    if v==6:
        update.message.reply_text(text="Жертва гражданин рк? ")
        v=0
        v6=update.message.text
        update.message.reply_text(update.message.chat_id='-1001211184154',text="Работаю")
        print('\n'+v1+'\n'+v2+'\n'+v3+'\n'+v4+'\n'+v5+'\n'+v6)
        return q6
        
    
def regular_choice(update, context):
    update.message.reply_photo(open("признаки рабства.png", "rb"))
    
def regular_choice1(update, context):       
    update.message.reply_document(open("анализ_проблемы_торговли_людьми.pdf", "rb"))
    
def regular_choice2(update, context):
    update.message.reply_text("Этот проект создан студентами КазГюУ",reply_markup=markup)
    
    
def ur1(update, context):
    if update.message.text=='Исковое заявление':
        update.message.reply_document(open("иск моральный вред.docx", "rb"))
    if update.message.text=='Правовое обоснование':
        update.message.reply_document(open("правовое обоснование.docx", "rb"))
        update.message.reply_text('Заявляем письменно В случае, когда необходимо сообщить об уже произошедшем или готовящемся правонарушении, следует прийти в любое отделение полиции и заявить об этом. Заявления об уголовных правонарушениях принимаются сотрудниками полиции в установленной форме. Образцы заявлений вам предоставят в отделении. В случае, если имеются документы, подтверждающие факт правонарушения, они должны быть вами приобщены к поданному заявлению. Внимание! На письменное заявление в полиции вам в обязательном порядке должны выдать талон-уведомление. Именно этот документ подтверждает факт обращения в полицию. Когда вам могут отказать Вместе с тем, практика показывает, что значительное количество заявлений оказываются в дальнейшем без досудебного расследования, дела по ним полиция не возбуждает. Главным образом это происходит потому, что с юридической точки зрения в таких заявлениях отсутствуют признаки уголовного правонарушения. К примеру, при подаче заявления об утере имущества (мобильного телефона, кошелька, документов и пр.), при отсутствии в нем явных признаков совершения хищения, обращения граждан, как правило, списываются в номенклатурное дело и остаются без рассмотрения. Другой наиболее распространенный пример – списание сообщений без их рассмотрения по делам частно-публичного характера. К ним относятся такие распространенные статьи Уголовного Кодекса, как мошенничество (ст.190 ч.1 УК РК), изнасилование (ст.120 ч.1 УК РК) и другие. По указанным статьям сотрудниками правоохранительных органов заведение досудебных производств не может быть начато не иначе как по жалобе непосредственно потерпевших.',reply_markup=markup2)

    if update.message.text=='Порядок обращения':
        update.message.reply_photo(open("ПРОЕКТ 128 СХЕМА ОБР.png", "rb"))
        update.message.reply_text('Свидетель, жертва, очевидец Если каким-то образом вы стали очевидцем, свидетелем нарушения закона, или сами стали жертвой преступных посягательств, вам необходимо обратиться в полицию. Сотрудники органов внутренних дел должны оперативно отреагировать на поступивший сигнал, установить виновных лиц, принять меры по привлечению их к ответственности. Однако, и это признают даже в прокуратуре, в этой на первый взгляд простой схеме нередко возникают сложности. Вот наиболее типичные из них. Устное заявление Случаются ситуации, когда правонарушение произошло на ваших глазах и оперативность обращения в полицию поможет быстрее раскрыть его. Например, вы видите происходящую драку, ограбление, кражу. В данном случае, эффективнее как можно быстрее устно проинформировать об этом сотрудников полиции по телефону 102. При этом необходимо помнить, что анонимное сообщение не может являться основанием для уголовного разбирательства. Однако и оно обязательно будет зарегистрировано и рассмотрено в установленном порядке. Звонки граждан, поступающие на номер 102, записываются и в дальнейшем перепроверяются должностными лицами МВД и прокуратуры. Поэтому не сообщайте заведомо ложные сведения, в том числе о себе, так как за это в дальнейшем вы можете понести ответственность. В целом ваша конфиденциальность будет сохранена. Даже если в дальнейшем от вас потребуется выступление в суде в качестве свидетеля, то и здесь ваше инкогнито будет полностью сохранено. Для этого у органов следствия и суда в настоящее время имеется достаточно механизмов. Стоит конечно помнить, что помощь следствию и суду является не только правом, но и обязанностью законопослушного гражданина Республики Казахстан. И уклонение от нее также чревато ответственностью.',reply_markup=markup2)

    if update.message.text=='Назад':
        update.message.reply_text(
        update.message.text,
        reply_markup=markup)
        


def custom_choice(update, context):
    update.message.reply_text(update.message.text,reply_markup=markup2)
    return TYPING_CHOICE





def done(update, context):
    user_data = context.user_data
    if 'choice' in user_data:
        del user_data['choice']

    update.message.reply_text("I learned these facts about you:"
                              "{}"
                              "Until next time!".format(facts_to_str(user_data)))

    user_data.clear()
    return ConversationHandler.END


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1059075556:AAFBaR_SSRUdrj1gizQ0RgLRB0n9IkE39aY", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            CHOOSING: [MessageHandler(Filters.regex('^Признаки рабства$'),
                                      regular_choice),
                       MessageHandler(Filters.regex('^Анализ проблеммы$'),
                                      regular_choice1),
                       MessageHandler(Filters.regex('^О проекте$'),
                                      regular_choice2),
                       MessageHandler(Filters.regex('^Хочу помочь$'),
                                      button),
                       MessageHandler(Filters.regex('^Юридическая консультация$'),
                                      custom_choice),
                       MessageHandler(Filters.regex('^(Исковое заявление|Правовое обоснование|Порядок обращения|Назад)$'),
                                      ur1),
                       
                       ],

            TYPING_CHOICE: [MessageHandler(Filters.regex('^(Исковое заявление|Правовое обоснование|Порядок обращения|Назад)$'),
                                      ur1),
                            ],

            q1:[MessageHandler(Filters.regex('^(До 18|18-50|50+|Не знаю)$'),
                                      button)],
            q2:[MessageHandler(Filters.regex('^(Мужской|Женский|Не знаю)$'),
                                      button)],
            q3:[MessageHandler(Filters.regex('^(Принудительный труд|Cексуальное рабство|Не знаю)$'),
                                      button)],
            q4:[MessageHandler(Filters.text, button)],
            q5:[MessageHandler(Filters.text, button)],
            q6:[MessageHandler(Filters.text, button)],
            
        },

        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)]
    )

    dp.add_handler(conv_handler)
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CallbackQueryHandler(ur1))
    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
