""" Здесь приводятся переменные, в которые закладывается текст значений инструкций.
 Далее формируются функции вывода сообщений """


TUTORIAL = ("📋 <b>ОСНОВНЫЕ КОМАНДЫ</b>:\n"
            "🔹 <b>/start</b> — стартовое меню \n"
            "🔹 <b>/help</b> — показать это сообщение\n\n\n"
            
            "<b><i> Инструкции пользователя </i></b>\n"
            "✏️ Порядок записи на тренировку, оповещения об оплате и удаления записи с тренировки <b>/train</b>\n\n"
            "📌 Описание меток ️⚠️✔️❌✅ и как формируется список участников на тренировку <b>/marks</b>\n\n"            
            "❓ Если у вас возникли вопросы, напишите нам! 😊 — <b>/bug</b>")


ADMIN_TUTORIAL = (
    "<b>АДМИНЫ <i>могут</i></b>:\n"
    "🔶 добавлять и удалять залы для тренировок;\n"
    "🔶 создавать и удалять запланированные тренировки;\n"
    "🔶 добавлять или удалять других админов;\n"
    "🔶 проводить верификацию оплаты участников.\n"
    "Все кнопки, доступные только админам, обозначены как 💠.\n\n"

    "<b>ВЕРИФИКАЦИЯ ОПЛАТЫ</b>\n"
    "Необходимо выбрать тренировку, нажать на кнопку подтверждения или опровержения оплаты. Далее "
    "через запятую перечислить в сообщении боту порядковые номера участников в списке и отправить его.\n"
    "🔘 <i>Важное примечание</i>\n"
    "Изменить статус участника при верификации вы сможете, если его текущий статус:\n"
    "🔸 равен ❌, ⚠️ или ✔️ в случае <i>подтверждения оплаты</i>;\n"
    "🔸 равен ✔️ в случае <i>опровержения оплаты</i>.\n"
    "Что обозначают эти статусы описано в <b>/marks</b>.\n"
    "⚡️<b><u>Для участников резервного списка верификация невозможна</u></b>.\n\n"
    
    "<b>ОСТАЛЬНЫЕ ФУНКЦИИ АДМИНА</b>\n"
    "Находясь в стартовом меню, нажимаете на соответствующую кнопку и следуете инструкциям бота.\n"
    "<b><i>В любой момент вы можете прервать процесс нажатием на кнопку возврата в стартовое меню.</i></b>"
)


SIGN_UP_FOR_TRAINING_TUTORIAL = (
    "Чтобы записаться на тренировку или удалиться, Вы должны находиться в стартовом меню далее следует "
    "выполнить следующие действия:\n"
    "<b>1</b>. Нажать на кнопку <i>'Выбрать тренировку.'</i>\n"
    "<b>2</b>. В появившемся списке нажмите на интересующую вас тренировку. "
    "Знаком 🟢 помечены те тренировки, на которые вы уже ранее записались.\n"
    "<b>3</b>. Перед вами появляется текущий список участников, заявившихся на тренировку.\n"
    "<b>4</b>. Нажать на кнопку записи на тренировку или удаления из нее.\n\n"
    
    "<b>💚 НАСТОЯТЕЛЬНО РЕКОМЕНДУЕТСЯ:</b>\n"
    "☑️ проводить оплату <b><i>заблаговременно</i></b> до наступления <u><b>ДЕДЛАЙНА</b></u>;\n"
    "☑️ после оплаты за тренировку оповестить бот. Для этого необходимо повторить вышеописанные "
    "<i>пп. 1 и 2</i> и выбрать тренировку со знаком 🟢. Под списком участников нажать на кнопку "
    "<i>'✔️ Я оплатил</i>'. <i>❗️ПОМНИТЕ❗️</i> оповестить бот об оплате можно только <b>ОДИН РАЗ</b> "
    "и только, если:\n"
    "  🔹 вы находитесь в <u>основном списке</u>;\n"
    "  🔹 ваш статус равен ⚠️;\n"
    "☑️ оповещать лично админа, если вы произвели оплату будучи в статусе ❌, поскольку "
    "оповещение бота в этом случае вам уже недоступно.\n\n"
    "<b>🚫 НАСТОЯТЕЛЬНО НЕ РЕКОМЕНДУЕТСЯ</b>:\n"
    "✖️ проводить оплату и оповещать бот незадолго до ДЕДЛАЙНА, иначе админ может не успеть проверить оплату;\n"
    "✖️ оповещать бот об оплате без фактической оплаты, иначе админ вам может присвоить статус ❌.\n\n"
    
    "‼️<b>ВАЖНО</b>\n"
    "<b>ДЕДЛАЙН</b> оплаты за тренировку наступает по <b><i>истечению суток</i></b> "
    "по состоянию на <i><b>2:00 </b></i> с момента записи участником на тренировку.\n"
    "<i>Например, если участник записался на тренировку 21 января в 15:00, то бот зафиксирует "
    "дедлайн 23 января в 2:00</i>\n\n"
    "🔴 Участник автоматически передвигается ботом в конец очереди, если при наступлении "
    "<b><i>ДЕДЛАЙНА</i></b>, статус участника равен ⚠️ или ❌. Расшифровка этих статусов приведена в <b>/marks</b>."
)


MARKS_DESCRIPTION = ('Рядом с каждым учатником <i>из основного списка</i> ставится соответствующая метка, '
                     'указывающая на статус оплаты за тренировку:\n'
                     '⚠️ участник не произвел оплату или в случае проведенной оплаты не оповестил бот нажатием кнопки <i>"✔️ Я оплатил"</i>;\n'
                     '✔️ участник оповестил бот об оплате;\n'
                     '❌ участник оповестил бот об оплате, но админ опроверг факт оплаты;\n'
                     '✅ админ подтвердил оплату.\n'
                     'Участники, пребывающие в <u>резерве</u>, не имеют меток.\n\n'
                     '❗<b>ВАЖНО</b>\n'
                     '1. Участники, у которых <u>при наступлении дедлайна</u> сохраняется статус ⚠️ или ❌, автоматически перемещаются ботом в конец очереди.\n'
                     '2. Уведомить бот об оплате можно <b><i>ТОЛЬКО</i></b> будучи пребывая в статусе ⚠️.\n'
                     '3. Если вы <b>ПРОВЕЛИ ОПЛАТУ</b> в <i><u>статусе ❌</u></i>, вам <u>ЖЕЛАТЕЛЬНО</u> уведомить об этом <u>ЛИЧНО</u> админа бота.\n'
                     'Основные рекомендации и условия дедлайна подробно описаны <b>/train</b>')
