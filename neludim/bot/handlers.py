
from functools import partial

from aiogram.types import (
    BotCommand,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

from neludim.const import (
    START_COMMAND,
    EDIT_INTRO_COMMAND,
    EDIT_NAME_COMMAND,
    EDIT_CITY_COMMAND,
    EDIT_LINKS_COMMAND,
    EDIT_ABOUT_COMMAND,
    CANCEL_COMMAND,
    EMPTY_COMMAND,
    PARTICIPATE_COMMAND,
    PAUSE_WEEK_COMMAND,
    PAUSE_MONTH_COMMAND,
    SHOW_CONTACT_COMMAND,
    CONFIRM_CONTACT_COMMAND,
    FAIL_CONTACT_COMMAND,
    CONTACT_FEEDBACK_COMMAND,

    EDIT_NAME_STATE,
    EDIT_CITY_STATE,
    EDIT_LINKS_STATE,
    EDIT_ABOUT_STATE,
    CONTACT_FEEDBACK_STATE,
    CONFIRM_STATE,
    FAIL_STATE,

    WEEK,
    MONTH,
)
from neludim.text import (
    day_month,
    user_url,
    user_mention
)
from neludim.obj import (
    Intro,
    User,
)


######
#
#  TEXT
#
########


########
#   COMMAND
#######


COMMAND_DESCRIPTIONS = {
    START_COMMAND: 'инструкция, список команд',

    EDIT_INTRO_COMMAND: 'поменять анкету',
    EDIT_NAME_COMMAND: 'поменять имя',
    EDIT_CITY_COMMAND: 'поменять город',
    EDIT_LINKS_COMMAND: 'поменять ссылки',
    EDIT_ABOUT_COMMAND: 'поменять "о себе"',

    PARTICIPATE_COMMAND: 'участвовать во встречах',
    PAUSE_WEEK_COMMAND: 'пауза на неделю',
    PAUSE_MONTH_COMMAND: 'пауза на месяц',

    SHOW_CONTACT_COMMAND: 'контакт, анкета собеседника',
    CONFIRM_CONTACT_COMMAND: 'договорились о встрече',
    FAIL_CONTACT_COMMAND: 'не договорились/не отвечает',
    CONTACT_FEEDBACK_COMMAND: 'как прошла встреча',

    CANCEL_COMMAND: 'отменить',
    EMPTY_COMMAND: 'оставить пустым',
}


def command_description(command):
    return f'/{command} - {COMMAND_DESCRIPTIONS[command]}'


COMMANDS_TEXT = f'''{command_description(EDIT_INTRO_COMMAND)}
{command_description(EDIT_NAME_COMMAND)}
{command_description(EDIT_CITY_COMMAND)}
{command_description(EDIT_LINKS_COMMAND)}
{command_description(EDIT_ABOUT_COMMAND)}

{command_description(PARTICIPATE_COMMAND)}
{command_description(PAUSE_WEEK_COMMAND)}
{command_description(PAUSE_MONTH_COMMAND)}

{command_description(SHOW_CONTACT_COMMAND)}
{command_description(CONFIRM_CONTACT_COMMAND)}
{command_description(FAIL_CONTACT_COMMAND)}
{command_description(CONTACT_FEEDBACK_COMMAND)}

{command_description(START_COMMAND)}'''


######
#  START
######


def start_text(schedule):
    return f'''Бот организует random coffee для сообщества @natural_language_processing.

Инструкция:
1. Заполни короткую анкету /{EDIT_INTRO_COMMAND}.
2. Дай согласия на участие во встречах /{PARTICIPATE_COMMAND}. В понедельник {day_month(schedule.next_week_monday())} бот подберёт собеседника, пришлёт анкету и контакт.
3. Заходи в закрытый чат для первых участников https://t.me/+-A_Q6y-dODY3OTli. Там разработчик бота @alexkuk принимает баг репорты, рассказывает о новых фичах.

{COMMANDS_TEXT}'''


######
#  OTHER
######


OTHER_TEXT = f'''Бот ответчает только на команды.

{COMMANDS_TEXT}'''


######
#  INTRO
######


EMPTY_SYMBOL = '∅'


def intro_text(intro):
    return f'''Имя: {intro.name or EMPTY_SYMBOL}
Город: {intro.city or EMPTY_SYMBOL}
Ссылки: {intro.links or EMPTY_SYMBOL}
О себе: {intro.about or EMPTY_SYMBOL}'''


def edit_intro_text(intro):
    return f'''{intro_text(intro)}

{command_description(EDIT_NAME_COMMAND)}
{command_description(EDIT_CITY_COMMAND)}
{command_description(EDIT_LINKS_COMMAND)}
{command_description(EDIT_ABOUT_COMMAND)}

{command_description(CANCEL_COMMAND)}
{command_description(EMPTY_COMMAND)}'''


EDIT_NAME_TEXT = '''Напиши своё настоящее имя. Собеседник поймёт, как к тебе обращаться.'''

EDIT_CITY_TEXT = '''Напиши город, в котором живёшь. Собеседник поймет предлагать офлайн встречу или нет.'''

EDIT_LINKS_TEXT = '''Накидай ссылок про себя: блог, твиттер, фейсбук, канал, подкаст. Собеседник поймёт чем ты занимаешься, о чём интересно спросить. Снимает неловкость в начале разговора.

Примеры
- http://lab.alexkuk.ru, https://github.com/kuk, https://habr.com/ru/users/alexanderkuk/
- https://www.linkedin.com/in/alexkuk/, https://vk.com/alexkuk
- http://val.maly.hk'''

EDIT_ABOUT_TEXT = '''Напиши о себе. Собеседник поймёт чем ты занимаешься, о чём интересно спросить. Снимает неловкость в начале разговора.

Что писать?
- Где учился?
- Где успел поработать? Чем занимался, самое важное/удивительное?
- Сфера интересов в NLP? Проекты, статьи.
- Личное, чем занимаешься кроме работы? Спорт, игры. Где успел пожить?

Например
"Закончил ШАД, работал в Яндексе в поиске. Сделал библиотеку Nile, чтобы удобно ворочать логи на Мап Редьюсе https://habr.com/ru/company/yandex/blog/332688/.

Автор проекта Наташа https://github.com/natasha. Работаю в своей Лабе https://lab.alexkuk.ru, адаптирую Наташу под задачи клиентов.

Живу в Москве в Крылатском. У нас тут мекка велоспорта. Умею сидеть на колесе и сдавать смену. Вожу экскурсии. Могу рассказать про путь от академизма к супрематизму."'''

TOP_CITIES = [
    'Москва',
    'Санкт-Петербург',
    'Киев',
    'Минск',
    'Лондон',
    'Берлин',
]


#####
#  CONTACT
#####


def participate_text(schedule):
    return f'Пометил, что участвуешь во встречах. В понедельник {day_month(schedule.next_week_monday())} бот подберёт собеседника, пришлёт анкету и контакт.'


PAUSE_TEXT = 'Поставил встречи на паузу. Бот не будет присылать контакты собеседников и напоминания.'


def no_contact_text(schedule):
    return f'Бот не назначил тебе собеседника. Бот составляет пары по понедельникам, очередной раунд {day_month(schedule.next_week_monday())}.'


def show_contact_text(user):
    return f'''Контакт собеседника в Телеграме: <a href="{user_url(user.user_id)}">{user_mention(user)}</a>.

{intro_text(user.intro)}

{command_description(CONFIRM_CONTACT_COMMAND)}
{command_description(FAIL_CONTACT_COMMAND)}
{command_description(CONTACT_FEEDBACK_COMMAND)}'''


CONFIRM_CONTACT_TEXT = f'Рад, что получилось договориться! Оставь фидбек после встречи /{CONTACT_FEEDBACK_COMMAND}.'


def fail_contact_text(schedule):
    return f'Жаль, что встреча не состоится. В понедельник {day_month(schedule.next_week_monday())} бот подберёт нового собеседника, пришлёт анкету и контакт.'


def contact_feedback_text(user, contact):
    return f'''Собеседник: <a href="{user_url(user.user_id)}">{user_mention(user)}</a>
Фидбек: {contact.feedback or EMPTY_SYMBOL}

Напиши фидбек своими словами или оставь оценку от 1 до 5, где 1 - очень плохо, 5 - очень хорошо.

/{EMPTY_COMMAND} - оставить пустым
/{CANCEL_COMMAND} - отменить'''


CONTACT_FEEDBACK_OPTIONS = '12345'


def contact_feedback_state_text(user, contact):
    return f'''Собеседник: <a href="{user_url(user.user_id)}">{user_mention(user)}</a>
Фидбек: {contact.feedback or EMPTY_SYMBOL}'''


#######
#
#   HANDLERS
#
######


######
#  START
######


async def handle_start(context, message):
    user = await context.db.get_user(message.from_user.id)
    if not user:
        user = User(
            user_id=message.from_user.id,
            username=message.from_user.username,
            intro=Intro(
                name=message.from_user.full_name,
            )
        )
        await context.db.put_user(user)

    await context.bot.set_my_commands(commands=[
        BotCommand(command, description)
        for command, description
        in COMMAND_DESCRIPTIONS.items()
    ])

    text = start_text(context.schedule)
    await message.answer(text=text)


#####
#  INTRO
######


async def handle_edit_intro(context, message):
    user = await context.db.get_user(message.from_user.id)
    text = edit_intro_text(user.intro)
    await message.answer(text=text)


async def handle_edit_name(context, message):
    user = await context.db.get_user(message.from_user.id)

    markup = None
    if not user.intro.name and message.from_user.full_name:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(message.from_user.full_name)

    await message.answer(
        text=EDIT_NAME_TEXT,
        reply_markup=markup
    )
    await context.db.set_chat_state(
        message.chat.id,
        EDIT_NAME_STATE
    )


async def handle_edit_city(context, message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for city in TOP_CITIES:
        markup.insert(city)

    await message.answer(
        text=EDIT_CITY_TEXT,
        reply_markup=markup
    )
    await context.db.set_chat_state(
        message.chat.id,
        EDIT_CITY_STATE
    )


async def handle_edit_links(context, message):
    await message.answer(text=EDIT_LINKS_TEXT)
    await context.db.set_chat_state(
        message.chat.id,
        EDIT_LINKS_STATE
    )


async def handle_edit_about(context, message):
    await message.answer(text=EDIT_ABOUT_TEXT)
    await context.db.set_chat_state(
        message.chat.id,
        EDIT_ABOUT_STATE
    )


def parse_command(text):
    if text.startswith('/'):
        return text.lstrip('/')


async def handle_edit_intro_states(context, message):
    state = await context.db.get_chat_state(message.chat.id)
    user = await context.db.get_user(message.from_user.id)

    command = parse_command(message.text)
    if command != CANCEL_COMMAND:
        if command != EMPTY_COMMAND:
            value = message.text
        else:
            value = None

        if state == EDIT_NAME_STATE:
            user.intro.name = value
        elif state == EDIT_CITY_STATE:
            user.intro.city = value
        elif state == EDIT_LINKS_STATE:
            user.intro.links = value
        elif state == EDIT_ABOUT_STATE:
            user.intro.about = value

        await context.db.put_user(user)

    text = edit_intro_text(user.intro)
    await message.answer(
        text=text,
        reply_markup=ReplyKeyboardRemove()
    )
    await context.db.set_chat_state(
        message.chat.id,
        state=None
    )


######
#  PARTICIPATE/PAUSE
#######


async def handle_participate(context, message):
    user = await context.db.get_user(message.from_user.id)

    user.agreed_participate = context.schedule.now()
    user.paused = None
    user.pause_period = None

    await context.db.put_user(user)

    text = participate_text(context.schedule)
    await message.answer(text=text)


async def handle_pause(context, message):
    user = await context.db.get_user(message.from_user.id)

    user.agreed_participate = None
    user.paused = context.schedule.now()

    command = parse_command(message.text)
    if command == PAUSE_WEEK_COMMAND:
        user.pause_period = WEEK
    elif command == PAUSE_MONTH_COMMAND:
        user.pause_period = MONTH

    await context.db.put_user(user)
    await message.answer(text=PAUSE_TEXT)


######
#  CONTACT
#########


async def handle_contact(context, message):
    user = await context.db.get_user(message.from_user.id)

    if not user.partner_user_id:
        text = no_contact_text(context.schedule)
        await message.answer(text=text)
        return

    key = (
        context.schedule.current_week_index(),
        user.user_id,
        user.partner_user_id
    )
    contact = await context.db.get_contact(key)
    if not contact:
        text = no_contact_text(context.schedule)
        await message.answer(text=text)
        return

    contact.user = user
    return contact


async def handle_show_contact(context, message):
    contact = await handle_contact(context, message)
    if not contact:
        return

    partner_user = await context.db.get_user(contact.partner_user_id)
    text = show_contact_text(partner_user)
    await message.answer(text=text)


async def handle_confirm_contact(context, message):
    contact = await handle_contact(context, message)
    if not contact:
        return

    contact.state = CONFIRM_STATE
    await context.db.put_contact(contact)

    await message.answer(text=CONFIRM_CONTACT_TEXT)


async def handle_fail_contact(context, message):
    contact = await handle_contact(context, message)
    if not contact:
        return

    contact.state = FAIL_STATE
    await context.db.put_contact(contact)

    text = fail_contact_text(context.schedule)
    await message.answer(text=text)


async def handle_contact_feedback(context, message):
    contact = await handle_contact(context, message)
    if not contact:
        return

    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=len(CONTACT_FEEDBACK_OPTIONS)
    )
    for option in CONTACT_FEEDBACK_OPTIONS:
        markup.insert(option)

    text = contact_feedback_text(contact.user, contact)
    await message.answer(
        text=text,
        reply_markup=markup
    )
    await context.db.set_chat_state(
        message.chat.id,
        CONTACT_FEEDBACK_STATE
    )


async def handle_contact_feedback_state(context, message):
    contact = await handle_contact(context, message)
    if not contact:
        return

    command = parse_command(message.text)
    if command != CANCEL_COMMAND:
        if command != EMPTY_COMMAND:
            contact.feedback = message.text
        else:
            contact.feedback = None

        await context.db.put_contact(contact)

    text = contact_feedback_state_text(contact.user, contact)
    await message.answer(
        text=text,
        reply_markup=ReplyKeyboardRemove()
    )
    await context.db.set_chat_state(
        message.chat.id,
        state=None
    )


######
#  OTHER
########


async def handle_other(context, message):
    await message.answer(text=OTHER_TEXT)


#######
#   SETUP
######


def setup_handlers(context):
    context.dispatcher.register_message_handler(
        partial(handle_start, context),
        commands=START_COMMAND,
    )

    context.dispatcher.register_message_handler(
        partial(handle_edit_intro, context),
        commands=EDIT_INTRO_COMMAND
    )
    context.dispatcher.register_message_handler(
        partial(handle_edit_name, context),
        commands=EDIT_NAME_COMMAND,
    )
    context.dispatcher.register_message_handler(
        partial(handle_edit_city, context),
        commands=EDIT_CITY_COMMAND,
    )
    context.dispatcher.register_message_handler(
        partial(handle_edit_links, context),
        commands=EDIT_LINKS_COMMAND,
    )
    context.dispatcher.register_message_handler(
        partial(handle_edit_about, context),
        commands=EDIT_ABOUT_COMMAND,
    )

    context.dispatcher.register_message_handler(
        partial(handle_participate, context),
        commands=PARTICIPATE_COMMAND
    )
    context.dispatcher.register_message_handler(
        partial(handle_pause, context),
        commands=[
            PAUSE_WEEK_COMMAND,
            PAUSE_MONTH_COMMAND,
        ]
    )

    context.dispatcher.register_message_handler(
        partial(handle_show_contact, context),
        commands=SHOW_CONTACT_COMMAND,
    )
    context.dispatcher.register_message_handler(
        partial(handle_confirm_contact, context),
        commands=CONFIRM_CONTACT_COMMAND,
    )
    context.dispatcher.register_message_handler(
        partial(handle_fail_contact, context),
        commands=FAIL_CONTACT_COMMAND,
    )
    context.dispatcher.register_message_handler(
        partial(handle_contact_feedback, context),
        commands=CONTACT_FEEDBACK_COMMAND,
    )

    # Every call to chat_states filter = db query. Place handlers
    # last. TODO Implement aiogram storage adapter for DynamoDB,
    # natively handle FSM

    context.dispatcher.register_message_handler(
        partial(handle_edit_intro_states, context),
        chat_states=[
            EDIT_NAME_STATE,
            EDIT_CITY_STATE,
            EDIT_LINKS_STATE,
            EDIT_ABOUT_STATE,
        ]
    )
    context.dispatcher.register_message_handler(
        partial(handle_contact_feedback_state, context),
        chat_states=CONTACT_FEEDBACK_STATE,
    )

    context.dispatcher.register_message_handler(
        partial(handle_other, context)
    )