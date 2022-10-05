# coding=utf-8

timeFormat_tooltip = (
    "Формат - Значення\n"
    "%a - Скорочена назва дня тижня\n"
    "%A - Повна назва дня тижня\n"
    "%b - Скорочена назва місяця\n"
    "%B - Повна назва місяця\n"
    "%c - Дата та час\n"
    "%d - День місяця [01,31]\n"
    "%H - Час (24-год. формат) [00,23]\n"
    "%I - Час (12-год. формат) [01,12]\n"
    "%j - День року [001,366]\n"
    "%m - Номер місяця [01,12]\n"
    "%M - Число хвилин [00,59]\n"
    "%p - До полудня або після (при 12-годинному форматі)\n"
    "%S - Число секунд [00,61]\n"
    "%U - Номер тижня в році (0 тиждень починається з неділі) [00,53]\n"
    "%w - Номер дня тижня [0(Sunday),6]\n"
    "%W - Номер тижня в році (0 тиждень починається с понеділка) [00,53]\n"
    "%x - Дата\n"
    "%X - Час\n"
    "%y - Рік без століття [00,99]\n"
    "%Y - Рік з століттям\n"
    "%Z - Часовий пояс\n"
    "%% - Знак '%'"
)

RESTART_TOOLTIP = "Для увімкнення/вимкнення необхідний перезапуск гри."

localization = {
    "configSelect": {
        "header": "Варіанти налаштувань",
        "selector": "Вибрати налаштування:",
        "donate_button_ua": "Підтримати розробку",
        "donate_button_paypal": "Підтримати через PayPal",
        "donate_button_patreon": "Підтримати через Patreon",
        "discord_button": "Discord сервер модифікації"
    },
    "main": {
        "header": "Налаштування без категорії",
        "DEBUG_MODE": "DEBUG_MODE",
        "showFriendsAndClanInEars": "Позначити друзів, гравців клану та себе в списках команд",
        "autoClearCache": "Очищати кеш гри після виходу",
        "autoClearCache_tooltip": "Очистка тимчасових файлів гри у папці: AppData/Roaming/Wargaming.net/WorldOfTanks.\n"
                                  "Папки модифікацій та налаштування, які зберігаються в тому ж місці, залишаться.",
        "removeShadowInPrebattle": "Прибрати затемнення таймеру на початку бою",
        "hideBadges": "Вимкнути відображення нашивок в бою",
        "hideBadges_tooltip": "Вимкнення відображення нашивок в бою у вухах, у вікні по клавіші Tab та на екрані "
                              "завантаження.",
        "hideClanAbbrev": "Вимкнути відображення клан тегу",
        "hideClanAbbrev_tooltip": "Вимкнення відображення клан тегу в бою у вухах, у вікні по клавіші Tab та на екрані "
                                  "завантаження.",
        "fps_enableFPSLimiter": "Увімкнути обмежувач FPS",
        "fps_enableFPSLimiter_tooltip": RESTART_TOOLTIP,
        "fps_maxFrameRate": "Максимальный FPS",
        "hideChatInRandom": "Вимкнути чат у випадкових боях",
        "hideChatInRandom_tooltip": "Повністю вимикає чат у випадкових боях.\nПрибирає форму чата і все, "
                                    "що з нею пов'язано.",
        "anonymousEnableShow": "Позначити гравців з прихованим іменем як 'team killer' (голубим кольором)",
        "anonymousEnableShow_tooltip": "Працює лише у випадку, якщо статистика гравців вимкнена.",
        "anonymousNameChange": "Змінити імена гравців з прихованим іменем на Anonymous",
        "useKeyPairs": "Використовувати парні Ctrl, Alt і Shift",
        "useKeyPairs_tooltip": "Після включення ліва і права клавіша будуть працювати як одна, незалежно від "
                               "того яку ви вибрали в налаштуваннях модуля. Не відноситься до модулю мінікарти.",
        "hide_dog_tags": "Вимкнути відображення жетонів в бою",
        "ignore_commanders_voice": "Ігнорувати озвучку командирів",
        "ignore_commanders_voice_tooltip": "Після включення буде примусово використовуватися стандартна озвучка"
                                           " екіпажу. Параметр замінить всі унікальні озвучки командирів "
                                           "на стандартну або із встановленого мода на озвучку.",
        "disable_score_sound": "Вимкнути звук при знищенні союзного чи ворожого танку",
        "premium_time": "Відображати точний час дії преміум аккаунту",
        "premium_time_tooltip": "Включення або вимкнення відбувається не моментально! Потрібно зачекати до 1 "
                                "хвилини або змінити вкладку гаражу",
        "auto_crew_training": "Автоматичне переключення галочки \"Пришвидшене навчання екіпажу\"",
        "auto_crew_training_tooltip": "Якщо \"Польова модернізація\" доступна для танка і вона не повністю прокачана, "
                                      "то галочка на екіпажі буде знята автоматично. Після її повної прокачки "
                                      "вам буде запропоновано увімкнути \"Пришвидшене навчання екіпажу\" або залишити "
                                      "все як є.",
        "do_not_buy_directives_for_currency_automatically": "Не купляти настанови за бони або срібло автоматично",
        "do_not_buy_directives_for_currency_automatically_tooltip":
            "Запобігає автоматичному поповненню настанов за бони або срібло, якщо їх не залишилось на складі. "
            "Модифікація також увімкне галочку \"Автоматичне поповнення\" у випадку, якщо їх запас є на складі.",
        "hide_hint_panel": "Вимкнути підказки в бою",
        "hide_field_mail": "Вимкнути польову пошту",
        "auto_return_crew": "Автоматичне повернення екіпажу",
        "auto_return_crew_tooltip": "Якщо на вибраному танку відсутній екіпаж, але він в наявності і не в бою "
                                    "на іншому танку, то екіпаж буде повернено в танк автоматично.",
        "disable_stun_sound": "Вимкнути звук оглушення від артилерії",
        "hide_main_chat_in_hangar": "Вимкнути спільний чат у гаражі",
        "hide_main_chat_in_hangar_tooltip": RESTART_TOOLTIP,
        "hide_button_counters_on_top_panel": "Вимкнути лічильники та підказки на кнопках в шапці гаражу.",
        "hide_button_counters_on_top_panel_tooltip": RESTART_TOOLTIP,
    },
    "statistics": {
        "header": "Налаштування статистики гравців та іконки танків",
        "statistics_enabled": "Увімкнути статистику гравців за рейтингом WTR",
        "statistics_change_vehicle_name_color": "Змінити колір назви танку в вухах на колір згідно з статистикою гравця",
        "statistics_enabled_tooltip": "Статистика буде відображатися на екрані завантаження, у вухах, у вікні по "
                                      "клавіші Tab.\nДля більш тонкого налаштування дивись файл statistics.json\n"
                                      "Доступні імена макросів: WTR, colorWTR, winRate, nickname, battles, clanTag",
        "icon_enabled": "Перефарбувати іконки танків в кольори класів техніки",
        "icon_enabled_tooltip": "Дана функція перефарбовує будь-які іконки техніки на екрані завантаження, у вухах, "
                                "у вікні по клавіші Tab в колір класів техніки.\nСила фільтра впливає на яскравість."
                                "\nРекомендована сила фільтра: -1.25",
        "icon_blackout": "Сила фільтра (яскравість)",
        "panels_full_width": "Ширина поля імені гравця (великі вуха)",
        "panels_cut_width": "Ширина поля імені гравця (малі вуха)",
    },
    "dispersion_circle": {
        "header": "Налаштування покращеного зведення та серверного прицілу",
        "circle_enabled": "Покращений круг зведення",
        "circle_use_lock_prediction": "Прилипання серверного прицілу при захваті цілі",
        "circle_extraServerLap": "Показувати серверний приціл як додатковий",
        "circle_extraServerLap_tooltip": "Увімкнення даної функції додасть додатковий круг зведення серверного прицілу "
                                         "до основного.",
        "circle_replaceOriginalCircle": "Замінити оригінальний круг зведення зменшеним",
        "circle_scale": "Множник розміру круга (1 - 100 %)",
        "circle_scale_tooltip": "Даний параметр впливає на те, яким буде круг сведения у підсумку.\n"
                                "Якщо його значення становить 1%, то круг буде мінімально можливим, "
                                "а при 100% - максимально, тобто без змін. "
                                "Не рекомендується встановлювати значення менше 65%.",
        "timer_enabled": "Включити таймер зведення",
        "timer_position_x": "Позиція таймера по горизонталі",
        "timer_position_y": "Позиція таймера по вертикалі",
        "timer_color": "Колір: Не зведений",
        "timer_done_color": "Колір: Повністю зведений",
        "timer_align": "Вирівнювання тексту"
    },
    "tank_carousel": {
        "header": "Налаштування каруселі танків",
        "carouselRows": "Кількість рядів каруселі танків",
        "carouselRows_tooltip": "Потребує увімкненої багаторядної каруселі в налаштуваннях гри.",
        "smallDoubleCarousel": "Примусово використовувати маленькі іконки"
    },
    "effects": {
        "header": "Налаштування візуальних ефектів",
        "noShockWave": "Прибрати потряхування камери при попаданні по танку",
        "noFlashBang": "Прибрати червоний спалах при отриманні пошкоджень",
        "noLightEffect": "Прибрати спалах і полум'я після пострілу",
        "noBinoculars": "Прибрати затемнення у режимі снайпера",
        "noSniperDynamic": "Вимкнути динамічну камеру у режимі снайпера"
    },
    "debug_panel": {
        "header": "Налаштування панелі FPS та PING",
        "debugText*text": "Текстове поле форматування панелі FPS та PING",
        "debugText*text_tooltip": "Макроси для панелі FPS та PING:\n"
                                  "%(PING)s - PING\n"
                                  "%(FPS)s - Поточний FPS\n"
                                  "%(fpsColor)s - колір FPS\n"
                                  "%(pingColor)s - колір PING/LAG.\n"
                                  "Підтримується HTML.",
        "debugText*x": "Позиція панелі по горизонталі",
        "debugText*y": "Позиція панелі по вертикалі",
        "debugGraphics*enabled": "Відображати графічний індикатор FPS та PING",
        "colors*fpsColor": "Колір макроса %(fpsColor)s",
        "colors*pingColor": "Колір макроса %(pingLagColor)s - Лаги відсутні",
        "colors*pingLagColor": "Колір макроса %(pingLagColor)s - Лаги присутні",
        "debugGraphics*fpsBar*color": "Колір графічного індикатору FPS",
        "debugGraphics*fpsBar*enabled": "Відображати графічний індикатор для FPS",
        "debugGraphics*pingBar*color": "Колір графічного індикатору PING",
        "debugGraphics*pingBar*enabled": "Відображати графічний індикатор для PING"
    },
    "battle_timer": {
        "header": "Налаштування таймеру боя",
        "timerTemplate": "Поле для форматування таймера",
        "timerTemplate_tooltip": "Доступні макроси:\n%(timer)s\n%(timerColor)s\nПідтримується HTML.",
        "timerColorEndBattle": "Колір макроса %(timerColor)s: залишається менше 2 хв.",
        "timerColor": "Колір макроса %(timerColor)s: більше 2 хв."
    },
    "clock": {
        "header": "Налаштування годиннику в ангарі та бою",
        "battle*enabled": "Відображати в бою",
        "battle*format": "Поле для форматування годинника в бою",
        "battle*format_tooltip": timeFormat_tooltip,
        "battle*x": "Позиція в бою по горизонталі",
        "battle*y": "Позиція в бою по вертикалі",
        "hangar*enabled": "Відображати в ангарі",
        "hangar*format": "Поле для форматування годинника в ангарі",
        "hangar*format_tooltip": timeFormat_tooltip,
        "hangar*x": "Позиція в ангарі по горизонталі",
        "hangar*y": "Позиція в ангарі по вертикалі"
    },
    "hp_bars": {
        "header": "Налаштування панелі здоров'я команд",
        "barsWidth": "Ширина полосок",
        "differenceHP": "Показувати різницю між загальними здоров'ям команд",
        "showAliveCount": "Показувати на панелі рахунку живих",
        "style": "Стиль панелі",
        "outline*enabled": "Увімкнути контур в стилі \"normal\"",
        "outline*color": "Колір контуру",
        "markers*enabled": "Карусель маркерів техніки",
        "markers*x": "Відстань по горизонталі від центру",
        "markers*x_tooltip": "Зеркально переміщає значки від центру на задану кількість пікселів",
        "markers*y": "Позиція по вертикалі від верху",
        "markers*y_tooltip": "Позиція маркерів по вертикалі від верху экрану.",
        "markers*showMarkers_hotkey": "Клавіша увімкнення/вимкнення маркерів",
        "markers*markersClassColor": "Пофарбувати значки каруселі по кольору класу техніки"
    },
    "armor_calculator": {
        "header": "Налаштування калькулятора наведеної броні",
        "position*x": "Позиція по горизонталі",
        "position*y": "Позиція по вертикалі",
        "template": "Поле для форматування",
        "display_on_allies": "Відображати на союзниках",
        "template_tooltip": "Формат макросів: %(ім'я)тип даних s:d:f.\n"
                            "s-рядок, d-десяткове число, f-число з плавающею точкою\n\n"
                            "Список доступних макросів:\n"
                            "%(countedArmor)d - Наведена броня\n"
                            "%(piercingPower)d - Пробиття снаряду з урахуванням відстані\n"
                            "%(piercingReserve)d - Запас пробиття після проходження броні\n"
                            "%(caliber)d - Калібр снаряду\n"
                            "%(message)s - Повідомлення із розділу \"messages\" в конфігураційному файлі\n"
                            "%(ricochet)s - Повідомлення про можливий рикошет\n"
                            "%(noDamage)s - Повідомлення про те, що пошкодження не буде. Снаряд попаде в модуль "
                            "оминаючи основну броню. Гусениця без пошкоджень, колесо без пошкоджень і т.д.\n"
                            "%(color)s - колір (дивись налаштування в розділі кольорів)\n"
    },
    "log_global": {
        "header": "Загальні налаштування логів",
        "logsAltmode_hotkey": "Перемикання логів в альтернативний режим",
        "wg_log_hide_assist": "Приховати пошкодження по розвідданим",
        "wg_log_hide_assist_tooltip": "Приховує пошкодження по розвідданим із детального лога гри",
        "wg_log_hide_block": "Приховати заблоковане пошкодження",
        "wg_log_hide_block_tooltip": "Приховує заблоковане пошкодження із детального лога гри",
        "wg_log_hide_critics": "Приховати критичні попадання",
        "wg_log_hide_critics_tooltip": "Приховує критичні попадання із детального лога гри",
        "wg_log_pos_fix": "Поставити логи гри на правильні місця",
        "wg_log_pos_fix_tooltip": "Міняє місцями логи отриманого і нанесеного пошкодження.\nОтриманий внизу, "
                                  "а нанесений зверху."
    },
    "log_total": {
        "header": "Налаштування сумарного логу ефективності гравця",
        "settings*inCenter": "Відображати лог в центрі екрану",
        "settings*x": "Позиція основного лога по горизонталі",
        "settings*y": "Позиція основного лога по вертикалі",
        "settings*align": "Вирівнювання:",
        "settings*align_tooltip": "Вирівнювання:\nleft - зліва\ncenter - по центру\nright - справа",
        "mainLogScale": "Масштабування лога"
    },
    "log_damage_extended": {
        "header": "Налаштування розширеного логу ефективності гравця",
        "settings*x": "Позиція детального лога по горизонталі",
        "settings*x_tooltip": "Відносно лівого списку гравців.",
        "settings*y": "Позиція детального лога по вертикалі",
        "settings*y_tooltip": "Відносно лівого списку гравців.",
        "settings*align": "Вирівнювання:",
        "settings*align_tooltip": "Вирівнювання:\nleft - зліва\ncenter - по центру\nright - справа",
        "reverse": "Розвернути лог",
        "reverse_tooltip": "Додавати новий рядок на початок логу.",
        "shellColor*gold": "Колір типу преміум снарядів",
        "shellColor*normal": "Колір типу звичайних снарядів"
    },
    "log_input_extended": {
        "header": "Налаштування розширеного логу отриманих пошкоджень",
        "settings*x": "Позиція детального лога по горизонталі",
        "settings*x_tooltip": "Відносно дамаг панелі.",
        "settings*y": "Позиція детального лога по вертикалі",
        "settings*y_tooltip": "Відносно дамаг панелі.",
        "settings*align": "Вирівнювання:",
        "settings*align_tooltip": "Вирівнювання:\nleft - зліва\ncenter - по центру\nright - справа",
        "reverse": "Розвернути лог",
        "reverse_tooltip": "Додавати новий рядок на початок логу.",
        "shellColor*gold": "Колір типу преміум снарядів",
        "shellColor*normal": "Колір типу звичайних снарядів"
    },
    "main_gun": {
        "header": "Налаштування основного калібру",
        "settings*x": "Позиція по горизонталі (від центру екрана)",
        "settings*y": "Позиція по вертикалі (від верхнього краю)",
        "settings*align": "Вирівнювання:",
        "settings*align_tooltip": "Вирівнювання:\nleft - зліва\ncenter - по центру\nright - справа"
    },
    "team_bases_panel": {
        "header": "Налаштування індикатору захоплення бази",
        "y": "Позиція смуги захоплення по вертикалі",
        "scale": "Масштабування полос захоплення",
        "boBases": "Увімкнути смуги захоплення з мода",
        "outline*enabled": "Увімкнути контур",
        "outline*color": "Колір контуру"
    },
    "vehicle_types": {
        "header": "Налаштування кольорів класів техніки",
        "vehicleClassColors*AT-SPG": "ПТ-САУ",
        "vehicleClassColors*SPG": "САУ",
        "vehicleClassColors*heavyTank": "Важкий танк",
        "vehicleClassColors*lightTank": "Легкий танк",
        "vehicleClassColors*mediumTank": "Середній танк",
        "vehicleClassColors*unknown": "Невідомо (ГК)"
    },
    "players_panels": {
        "header": "Налаштування панелей з списком гравців",
        "players_damages_enabled": "Пошкодження гравців в списках команд",
        "players_damages_hotkey": "Клавіша для відображення пошкоджень",
        "players_damages_settings*x": "Позиція тексту по горизонталі",
        "players_damages_settings*y": "Позиція тексту по вертикалі",
        "players_bars_enabled": "Здоров'я гравців у вухах",
        "players_bars_settings*players_bars_bar*outline*enabled": "Увімкнути контур",
        "players_bars_settings*players_bars_bar*outline*customColor": "Користувацький колір контуру",
        "players_bars_settings*players_bars_bar*outline*color": "Колір контуру",
        "players_bars_settings*players_bars_bar*outline*alpha": "Прозорість контуру",
        "players_bars_hotkey": "Клавіша відображення здоров'я",
        "players_bars_classColor": "Пофарбувати смуги здоров'я у вухах по кольору типу техніки",
        "players_bars_on_key_pressed": "Відображати смуги тільки по натисканню клавіші",
        "panels_spotted_fix": "Виправити розмір і позицію лампочок виявлення"
    },
    "zoom": {
        "header": "Налаштування режиму снайпера",
        "disable_cam_after_shot": "Вимикати режим снайпера після пострілу",
        "disable_cam_after_shot_tooltip": "Автоматично перемикає камеру в режим аркади після пострілу, "
                                          "якщо калібр гармати більше 60мм.",
        "disable_cam_after_shot_latency": "Затримка автоматичного вимкнення режиму снайпера",
        "disable_cam_after_shot_skip_clip": "Не виходити із режиму, якщо є касетна система зарядження",
        "dynamic_zoom*zoomXMeters": "Чутливість наближення в метрах",
        "dynamic_zoom*zoomXMeters_tooltip": "Автоматичний вибір означає, що відстань до цілі в метрах ділене на "
                                            "чутливість буде використовуватись для вибору кратності зуму.\n"
                                            "За замовчуванням на кожні 20 метрів приходиться х1 "
                                            "кратності наближення. Чим менше показник чутливості - "
                                            "тим більше кратність наближення в співвідношенні (дистанція до "
                                            "цілі/дистанція для збільшення кратності).",
        "dynamic_zoom*enabled": "Автоматичний вибір кратності наближення",
        "dynamic_zoom*steps_only": "Переміщатися тільки по фіксованим крокам",
        "dynamic_zoom*enabled_tooltip": "Якщо дана функція увімкнена, то <b>фіксований параметр</b> "
                                        "працювати не буде.",
        "zoomSteps*enabled": "Замінити кратності зуму",
        "zoomSteps*steps": "Кроки кратності зуму",
        "zoomSteps*steps_tooltip": "Кроки кратності зуму потрібно записати через кому і пробіл або лише кому. "
                                   "Підтримується будь-яка кількість кроків."
    },
    "arcade_camera": {
        "header": "Налаштування командирської камери",
        "max": "Максимальне віддалення (за замовчуванням - 25)",
        "min": "Максимальне наближення (за замовчуванням - 2)",
        "startDeadDist": "Дистанція камери під час старту/знищення (за замовчуванням - 15)",
        "scrollSensitivity": "Чутливість прокрутки (за замовчуванням - 4)"
    },
    "strategic_camera": {
        "header": "Налаштування камери артилериста",
        "max": "Максимальне віддалення (за замовчуванням - 100)",
        "min": "Максимальное наближення (за замовчуванням - 40)",
        "scrollSensitivity": "Чутливість прокрутки (за замовчуванням - 10)"
    },
    "flight_time": {
        "header": "Налаштування часу польоту снаряду та дистанція до цілі",
        "x": "Позиція тексту по горизонталі",
        "x_tooltip": "Положення від центру екрану.",
        "y": "Позиція тексту по вертикалі",
        "y_tooltip": "Положення від центру екрану.",
        "spgOnly": "Відображати час польоту тільки на артилерії",
        "template": "Шаблон строки. Макроси: %(flightTime).1f , %(distance).1f",
        "wgDistDisable": "Сховати базову дистанцію в прицілі",
        "align": "Вирівнювання тексту"
    },
    "save_shoot": {
        "header": "Налаштування блокування пострілів по союзникам і знищеним",
        "block_on_destroyed": "Заблокувати постріл по знищеним",
        "msg": "Повідомлення про блокування пострілу",
        "msg_tooltip": "Дане повідомлення відображається лише у випадку блокування пострілу по союзнику і "
                       "видно лише гравцю."
    },
    "minimap": {
        "header": "Налаштування міні-карти",
        "zoom": "Увімкнути збільшення міні-карти в центр",
        "permanentMinimapDeath": "Завжди показувати знищених на карті",
        "showDeathNames": "Відображати імена знищених танків",
        "real_view_radius": "Прибрати обмеження кругу огляду більше 445м",
        "yaw_limits": "Відображати кути горизонтального наведення на всій техніці, де можливо",
        "zoom_hotkey": "Клавіша для збільшення карти"
    },
    "shadow_settings": {
        "header": "Налаштування тіней тексту",
        "inner": "Використовувати внутрішнє світіння (inner glow)",
        "knockout": "Використовувати ефект просвічування (knockout)",
        "blurX": "Ступінь розмиття тіні по горизонталі",
        "blurY": "Ступінь розмиття тіні по вертикалі",
        "alpha": "Значення прозорості кольору",
        "color": "Колір тіні та світіння",
        "strength": "Ступінь вдавлення або просвічування.",
        "blurY_tooltip": "Значення степені двійки (тобто 2, 4, 8, 16, 32 і т.д.) оптимізуються і виконуються "
                         "швидше, ніж інші.",
        "blurX_tooltip": "Значення степені двійки (тобто 2, 4, 8, 16, 32 і т.д.) оптимізуються і виконуються "
                         "швидше, ніж інші.",
        "inner_tooltip": "Тінь тексту буде мати внутрішнє світіння у випадку, якщо налаштування увімкено, інакше - "
                         "зовнішнє світіння навколо контуру тексту.",
        "knockout_tooltip": "Тінь тексту буде мати заливку об'єкту прозорою і робить видимим колір фону, тобто "
                            "ефект просвічування.",
        "strength_tooltip": "Чим вище значення, тим більше насичений колір тіні і тим сильнішим контраст між "
                            "світінням і фоном. Підтримувані значення від 0 до 255. За замовчуванням — 2."
    },
    "colors": {
        "header": "Глобальні налаштування кольорів",
        "armor_calculator*green": "Наведена броня: Шанс пробиття 100%",
        "armor_calculator*orange": "Наведена броня: Шанс пробиття 50%",
        "armor_calculator*red": "Наведена броня: Шанс пробиття 0%",
        "armor_calculator*yellow": "Наведена броня: Шанс пробиття 50% (режим колірної сліпоти)",
        "armor_calculator*purple": "Наведена броня: Шанс пробиття 0% (режим колірної сліпоти)",
        "global*ally": "Глобальний колір: союзники",
        "global*bgColor": "Колір фону панелей",
        "global*enemyColorBlind": "Глобальний колір: супротивники (колірна сліпота)",
        "global*enemy": "Глобальний колір: супротивники",
        "global*alpha": "Прозорість панелей",
        "global*alpha_tooltip": "0 - прозорий.\n1 - не прозорий.",
        "global*bgAlpha": "Прозрачность фону панелей",
        "global*bgAlpha_tooltip": "0 - прозорий.\n1 - не прозорий.",
        "global*deadColor": "Глобальний колір: знищений",
    },
    "service_channel_filter": {
        "header": "Налаштування фільтру повідомлень в системному каналі",
        "sys_keys*CustomizationForCredits": "Налаштування техніки за кредити",
        "sys_keys*CustomizationForGold": "Налаштування техніки за золото",
        "sys_keys*DismantlingForCredits": "Демонтаж обладнання за кредити",
        "sys_keys*DismantlingForCrystal": "Демонтаж обладнання за бони",
        "sys_keys*DismantlingForGold": "Демонтаж обладнання за золото",
        "sys_keys*GameGreeting": "Вітання",
        "sys_keys*Information": "Інформаційні повідомлення",
        "sys_keys*MultipleSelling": "Продажа кількох предметів",
        "sys_keys*PowerLevel": "Дослідження модулів і техніки",
        "sys_keys*PurchaseForCredits": "Покупки за кредити",
        "sys_keys*PurchaseForCrystal": "Покупки за бони",
        "sys_keys*PurchaseForGold": "Покупки за золото",
        "sys_keys*Remove": "Видалення предмету",
        "sys_keys*Repair": "Ремонт",
        "sys_keys*Restore": "Відновлення",
        "sys_keys*Selling": "Продажа одного предмету",
        "sys_keys*autoMaintenance": "Автоматичне обслуговування техніки",
        "sys_keys*customizationChanged": "Налаштування змінено"
    },
    "service": {
        "name": "Battle Observer - v{0}",
        "description": "Відкрити налаштування мода Battle Observer",
        "windowTitle": "Налаштування мода Battle Observer - v{0}",
        "buttonOK": "OK",
        "buttonCancel": "Відміна",
        "buttonApply": "Застосувати",
        "enableButtonTooltip": "{HEADER}ВКЛ/ВИКЛ{/HEADER}{BODY}Увімкнути/Вимкнути модуль{/BODY}"
    },
    "sixth_sense": {
        "header": "Налаштування лампи шостого відчуття",
        "showTimer": "Відображати таймер",
        "lampShowTime": "Тривалість в секундах",
        "lampShowTime_tooltip": "<b>Як довго видно виявлену ціль?</b>\nПісля того як промені видимості одного "
                                "танку перетнулись з оглядовими точками іншого, то перший танк буде залишатися видимим "
                                "навіть якщо промені видимості більше не взаємодіють з оглядовими точками. Звичайний "
                                "час, протягом якого танк залишається видимим — 10 секунд, але це время можна як "
                                "зменшити до 8, так і збільшити до 16-18 секунд в залежності от встановленого на "
                                "танк обладнання, навичок та умінь членів екіпажу та настанов.",
        "playTickSound": "Програвати звук таймеру"
    },
    "distance_to_enemy": {
        "header": "Налаштування дистанції до найближчого виявленого ворогу",
        "x": "Позиція текста по горизонталі",
        "x_tooltip": "Положення від центру екрана",
        "y": "Позиція текста по вертикалі",
        "y_tooltip": "Положення від центру екрана",
        "template": "Шаблон строки. Макроси: %(distance)s, %(name)s",
        "align": "Вирівнювання тексту"
    },
    "own_health": {
        "header": "Налаштування здоров'я техніки гравця",
        "x": "Позиція текста по горизонталі",
        "x_tooltip": "Положення від центру екрана",
        "y": "Позиция текста по Вертикали",
        "y_tooltip": "Положення від центру екрана",
        "template": "Шаблон строки. Макроси: %(cur_health)s, %(max_health)s, %(per_health)s",
        "align": "Вирівнювання тексту"
    },
    "crewDialog": {
        "enable": "Увімкнути пришвидшене навчання екіпажу?",
        "disable": "Вимкнути пришвидшене навчання екіпажу?",
        "notAvailable": "Польова модернізація недоступна для даної техніки",
        "isFullXp": "Ви набрали необхідну кількість досвіду для повної прокачки польової модернізації",
        "isFullComplete": "Ви прокачали польову модернізацію до максимально можливого рівня",
        "needTurnOff": "У вас не прокачана польова модернізація.\nРекомендовано вимкнути пришвидшене навчання екіпажу."
    },
}
