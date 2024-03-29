init:
    $ mods['test']=u'БПЛ: начало'
    $ ps = Character(u"Пасюк Лошадкин", color='#BDB76B')
    $ br = Character(u"Брит", color='#54c8ff')
    $ pl = Character(u"Полунин", color='#d9e835')
    $ brit_nows_egor = 0
    image bg noutbuk_pasuk = 'mods/shlak/sprites/comp_pasuka.jpeg'
    image bg noutbuk_brit = 'mods/shlak/sprites/comp_brita.jpeg'
    image bg bus_morning = 'mods/shlak/sprites/bus_morning.png'
label test:
    play music music_list['raindrops']
    scene bg black
    "Это был обычный день. Совсем уж обычный. За окном шел снег, завывала вьюга. Часы тикали четвертый час."
    "Три друга-программиста переписывались в Телеграмме. Не будем приводить их имена, назовем их никнеймы: Брит, Полунин и Пасюк Лошадкин."
    "Полунин и Пасюк как всегда учили Брита программированию. Но Бриту сложно давалось это занятие, и он уже совсем отчаялся разобраться в нем."
    "За окном тем временем совсем стемнело. Полунин ощутил резкий голод, и пошел ужинать. Лошадкин ушел подро... по своим делам."
    scene bg noutbuk_brit
    th 'Триггеры это просто пиздец.'
    th 'А о монге и говорить нечего!'
    th 'Да и Полунин с Пасюком поняли, что они за меня пишут код, и постоянно теперь кидают гайды.'
    th 'Вся надежда на Юльку...'
    pl 'Брит, ебас, ты где? Я пожру и приду.'
    br 'Да бля, устал я от этой ебалы.'
    br 'Я спать.'
    "Брит не хотел оставаться долго за комьютером."
    br "Как меня все это заебало! Почему это настолько сложно? Тупой компьютер!"
    with vpunch
    "*Звуки удара*"
    br "Ты еще и бьешся!"
    br "Пойду в ванную."
    scene bg semen_room with dissolve
    "Брит только встал из-за компьютера, но вдруг наступил на что-то липкое под своим столом, и подскользнулся. Он ударился головой об кровать."
    with vpunch
    br "Ай, бля! Наебнулся!"
    show blink
    scene bg black
    hide blink
    "..."
    scene bg noutbuk_pasuk with dissolve
    "Пасюк же тем временем думал над тем, уделить ли ещё немного времени на поиск гайдов для Брита, или пойти посмотреть видосы на ютубе."
    "Лень победила."
    th "Ай ладно, пусть теперь Полунин помогает, я свою часть выполнил."
    scene bg semen_room with dissolve
    "Он встал из-за стола, выключил ноутбук, и лёг на кровать."
    "В последнее время почти все мысли его были об одном - чем себя занять?"
    "Ведь вот уже пол года он находится в академическом отпуске по причине частых болезней. Всё общение его ограничивалось мессенджером Telegram, да парой бесед в нём - из дома выходил он только за продуктами."
    th "Надоело... На ютубе ничего интересного. Компьютер сгорел. Вот вроде ничем не занимаюсь, а всё равно устаю! Что будет, когда начнётся учёба?"
    th "Да я уже и не надеюсь окончить колледж, с такой-то мотивацией... А что потом? Найду какую-нибудь непыльную работу, чтобы на жизнь хватало - и буду работать до конца своих дней..."
    th "Капец как интересно. Ну хотя бы чувствую себя полезным, помогая Бриту с программированием - хоть кто-то адекватно воспользуется знаниями питона..."
    th "Так, хватит - эти мысли мне ничем не помогут, только настроение испорчу."
    "Пасюк от нечего делать решил пойти на кухню. Открыл холодильник, и стал смотреть внутрь - как будто от того, что он раз за разом открывает его, внутри что-то меняется."
    th "Опять есть нечего. Придётся одеваться и идти в магазин."
    "От этой мысли он скривился - вместо того, чтобы лежать в кровати, сейчас придётся одеваться, выходить на улицу, тратить силы..."
    th "Ну ничего не поделаешь, поiхали."
    "Он быстро накинул куртку, надел ботинки и вышел на улицу."
    scene bg bus_stop with dissolve2
    th "Да, зимние улицы красивые. Жаль, что когда есть какие-то дела помимо похода в магазин, то просто не обращаешь на это внимания."
    th "А ведь закончится мой отпуск, и я вернусь к привычному образу жизни - учеба-дом-сон-учеба. А потом учёба заменится на работу, но глобально всё равно ничего не поменяется."
    "За всеми этими мыслями он не заметил, как подошёл к пешеходному переходу. Резкий свет в глаза, звук торможения - но полностью затормозить машина не успевает."
    with vpunch
    # звук удара
    show blink
    scene bg black
    hide blink
    "..."
    scene bg noutbuk_brit with dissolve
    "А полунин тем временем доел, и вернулся за комп, и написал бриту подробную инструкцию про то, как использовать датабазу."
    th "Надеюсь, он не тупо скопирует, а попытается разобраться."
    "Вечерело. Так как Брит и Пасюк вышли из сети, Полунин решил, что ему пора спать."
    "..."
    "Только он хотел лечь спать, как услышал ругань соседей."
    th "Опять эти ненормальные ругаются..."
    "Такое происходило часто - набухаются, и выясняют отношения на весь дом."
    "Сверху гремело все громче. Полунину не понравилось, что ему придется всю ночь пытаться заснуть под крики и грохот."
    pl "~Пойду попробую их успокоить~"
    scene bg semen_room with dissolve
    "Полунин открыл входную дверь своей квартиры, и направился на этаж выше, к той самой двери"
    # звук звонка
    "Из квартиры выбежал муж. В руках у него был заряженный револьвер."
    u"Сосед" "Ты кто такой? Это ты любовник моей жены, да? Это ты ее трахнул?"
    pl "Подождите, подождите, я всего лишь ваш сосед!"
    u"Сосед" "Это ты, падла!"
    "*звуки выстрела*"
    with vpunch
    scene bg black
    $ backdrop = "days"
    $ new_chapter(1, u"Мой мод. День первый.")
    scene bg int_bus
    th "Голова болит...{w} Сколько я вчера выпил? Вроде вообще не пил..."
    th "Да и вообще, как я уснул в сидячем положении?"
    scene bg int_bus
    hide blink
    show unblink
    th "Ёб..."
    "Открыв глаза, он понял, что находится не у себя в квартире, а в салоне какого-то автобуса, причём за окном было самое настоящее {b}ЛЕТО!{/b}"
    th "Какого..."
    "Мягко говоря, он офигел. Осмотревшись, он понял, что не один в автобусе - спереди сидели ещё 2 человека, примерно его возраста."
    th "Ну дела... Может, у них спросить?"
    th "А что спрашивать?"
    menu:
        "Вы кто такие?":
            jump vi_kto
        "Мы где?":
            jump mi_gde
        "Вы охуели?":
            jump vi_ahueli
label vi_kto:
    "Брит встал со своего места, подошёл к одному из пассажиров и потряс его."
    "Тот во сне сказал что-то про ослов, и открыл глаза."
    me "Чел, а ты кто?"
    u"Парень" "Егор... Стоп, а ты кто? И что происходит?"
    me "Егор... Что-то знакомое."
    $ brit_nows_egor += 1
    "Тут он посмотрел в окно, и на его лице прочиталась нескрываемая эмоция, обозначающая \"{b}ЧТО БЛЯТЬ!?\""
    u"Егор" "А МЫ ВООБЩЕ ГДЕ!?"
    me "Я сам не знаю, думал ты знаешь"
    u"Егор" "Как будто мы вчера очень хорошо набухались... Надо вспомнить, что было до этого."
    "Они начали вспоминать."
    u"Егор" "Я, кажется, вспомнил! Меня сбила машина по дороге в магазин..."
    "Он ощупал себя"
    u"Егор" "Но как? Я вроде цел, даже не сломано ничего."
    "Он встал и подвигал конечностями."
    u"Егор" "Чертовщина какая-то!"
    "В этот момент послышались звуки с переднего сиденья."
    jump ai_bolno
label mi_gde:
    br "Мы где?"
    "Брит встал со своего места, подошёл к одному из пассажиров и потряс его."
    u"Парень" "Я... ослов... ослы..."
    me "Эм, привет, а мы где?"
    "Неизвестный проснулся и осмотрелся."
    u"Парень" "Походу в автобусе..."
    me "Да я и сам вижу. А какого хрена?"
    u"Парень" "Мы.. В автобусе.. КАКОГО ХРЕНА?"
    me "Я проснулся, и увидел..."
    u"Парень" "КАК Я ЗДЕСЬ ОКАЗАЛСЯ?"
    me "Хз. Нужно вспомнить, как мы тут оказались."
    u"Парень" "Голова раскалывается... Вспомнил, я пошел в магазин за едой, а меня сбила машина..."
    jump ai_bolno
label vi_ahueli:
    me "Вы охуели? Куда вы меня затащили?"
    u"Парень" "Я... ослов... ослы..."
    me "Алло, ебать. Вы офигели?"
    with vpunch
    me "Просыпайся, шашлык."
    u"Парень" "Ай!"
    with vpunch
    me "Да не бейся! Я тебя разбудить хотел."
    u"Парень" "Ты кто ебать? Где я?"
    me "Ты меня сюда приволок, и потом спрашиваешь, куда?"
    th "Хотя как он мога меня украсть... Он же спал..."
    u"Парень" "Ебаклак?"
    u"Второй парень" "Бляяяя... Голова раскалывается..."
    jump ai_bolno

label ai_bolno:
    u"Второй парень" "Блиаааа... Голова раскалывается..."
    me "Еще один. Бля, тоже парень."
    u"Второй парень" "Кто здесь?"
    u"Парень" "Два негра, ебать тебя в жопу будут."
    "Парень вскочил."
    u"Второй парень" "Зачем так пугать?! Далбаебы?"
    me "Да."
    u"Второй парень" "Зашибись. Где я?"
    u"Парень" "В пизде."
    me "В автобусе."
    u"Второй парень" "А где сосед?"
    me "Какой сосед?"
    u"Второй парень" "Который с револьвером на меня хотел напасть."
    u"Парень" "Челик, тебе бы провериться не мешало у психиатра"
    me "Как и нам."
    u"Парень" "Как и нам."
    u"Второй парень" "Ладно, раз уж мы братья по несчастью, то скажите хоть как вас зовут. Я Дима"
    u"Егор" "Я Егор."
    me "Я Брит."
    "Ответил Брит совершенно машинально."
    u"Дима" "Брит? Стой, подожди, а равзе тебе не Полунин с Пасюком вчера помогали?"
    u"Егор" "Пасюком? Откуда ты знаешь Пасюка?"
    pl "Так я же Полунин!"
    me "ЕБАТЬ ТАК ВСТРЕЧА!"
    ps "Не ори, ебас."
    pl "Отлично ебать. Кстати... Мы же в автобусе?"
    ps "Ну да."
    pl "Он едет?"
    ps "Да заебал, говори короче."
    pl "Кароч, вы водителя видели?"
    me "Нет..."
    pl "Пошли посмотрим. Кто пойдет первым?"
    menu:
        "Я":
            jump i_go_to_voditel
        "Полунин":
            jump pl_go_to_voditel
        "Пасюк":
            jump ps_go_to_voditel

label i_go_to_voditel:
    me "Я пойду."
label pl_go_to_voditel:
    me "Иди ты."
label ps_go_to_voditel:
    me "Пасюк, иди ты."
