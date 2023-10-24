# This Python file uses the following encoding: utf-8
import sqlite3

# подключение к базе данных
conn = sqlite3.connect('misis.db')

# создает объект курсора
cursor = conn.cursor()

# создаем таблицу c направлениями
cursor.execute('''CREATE TABLE specializations
            	(id INTEGER PRIMARY KEY, name TEXT, min_score_platka INTEGER, min_score_budget INTEGER)''')

info = [(1,'45.03.02 Лингвистика', 190, 286),
        (2,'03.03.02 Физика',190, 236),
        (3,'11.03.04 Электроника и наноэлектроника',190, 217),
        (4,'22.03.01 Материаловедение и технологии материалов',190, 206),
        (5,'28.00.00 Нанотехнологии и наноматериалы',190, 234),
        (6,'01.03.04 Прикладная математика',190, 270),
        (7,'09.00.00 Информатика и вычислительная техника',190, 273),
        (8,'13.03.02 Электроэнергетика и электротехника',190, 223),
        (9,'21.00.00 Геотехнологии',190, 200),
        (10,'15.03.02 Технологические машины и оборудование',190, 186),
        (11,'22.03.02 Металлургия',190, 201),
        (12,'38.00.00 Экономика и управление',190, 268),
        (13,'38.03.06 Торговое дело',190, 268),
        (14,'38.03.05 Бизнес-информатика',190, 270)
        ]

# добавляем новую запись в таблицу specializations
cursor.executemany('INSERT INTO specializations (id, name, min_score_platka, min_score_budget) VALUES (?, ?, ?, ?)', info)

# создаем таблицу с предметами
cursor.execute('''CREATE TABLE subjects (id INTEGER, subjects1 TEXT, subjects2 TEXT, subjects3 TEXT)''')

subjects_info = [(1, 'Иностранный', 'Русский', 'Обществознание'),
                 (1, 'Иностранный', 'Русский', 'История'),
                 (2, 'Математика', 'Русский', 'Физика'),
                 (3, 'Математика', 'Русский', 'Физика'),
                 (3, 'Математика', 'Русский', 'Химия'),
                 (3, 'Математика', 'Русский', 'Информатика'),
                 (4, 'Математика', 'Русский', 'Физика'),
                 (4, 'Математика', 'Русский', 'Химия'),
                 (4, 'Математика', 'Русский', 'Информатика'),
                 (5, 'Математика', 'Русский', 'Физика'),
                 (5, 'Математика', 'Русский', 'Химия'),
                 (5, 'Математика', 'Русский', 'Информатика'),
                 (6, 'Математика', 'Русский', 'Физика'),
                 (6, 'Математика', 'Русский', 'Химия'),
                 (6, 'Математика', 'Русский', 'Информатика'),
                 (7, 'Математика', 'Русский', 'Физика'),
                 (7, 'Математика', 'Русский', 'Химия'),
                 (7, 'Математика', 'Русский', 'Информатика'),
                 (8, 'Математика', 'Русский', 'Физика'),
                 (8, 'Математика', 'Русский', 'Химия'),
                 (8, 'Математика', 'Русский', 'Информатика'),
                 (9, 'Математика', 'Русский', 'Физика'),
                 (9, 'Математика', 'Русский', 'Химия'),
                 (9, 'Математика', 'Русский', 'Информатика'),
                 (10, 'Математика', 'Русский', 'Физика'),
                 (10, 'Математика', 'Русский', 'Химия'),
                 (10, 'Математика', 'Русский', 'Информатика'),
                 (11, 'Математика', 'Русский', 'Физика'),
                 (11, 'Математика', 'Русский', 'Химия'),
                 (11, 'Математика', 'Русский', 'Информатика'),
                 (12, 'Математика', 'Русский', 'Обществознание'),
                 (12, 'Математика', 'Русский', 'Информатика'),
                 (12, 'Математика', 'Русский', 'Иностранный'),
                 (13, 'Математика', 'Русский', 'Обществознание'),
                 (13, 'Математика', 'Русский', 'Информатика'),
                 (13, 'Математика', 'Русский', 'Иностранный'),
                 (14, 'Математика', 'Русский', 'Обществознание'),
                 (14, 'Математика', 'Русский', 'Информатика')]

# добавляем новую запись в таблицу subjects
cursor.executemany('INSERT INTO subjects (id, subjects1, subjects2, subjects3) VALUES (?, ?, ?, ?)', subjects_info)

# создаем таблицу с описанием направления
cursor.execute('''CREATE TABLE specializations_description (id INTEGER, description TEXT)''')

description = [(1, 'Зачем изучать лингвистику в одном из лучших технических университетов? Знание основ инженерных наук сделает возможной вашу карьеру в производственных компаниях и научно-исследовательских центрах. Разнообразие уникальных образовательных треков позволит вам стать редким специалистом на рынке труда. Иностранные преподаватели — носители языка и 20-летняя экспертиза кафедры помогут овладеть английским языком на уровне С1 и выше, а также еще одним языком на уровне В2 и выше.\nУзнать подробности: https://misis.ru/applicants/admission/baccalaureate-and-specialty/faculties/lingv/'),
               (2, 'Хотите учиться на одной из лучших программ по физике в России и в мире? Мы более 90 лет готовим кадры высшей квалификации — ученых-физиков международного уровня! На базе НИТУ МИСИС совместно с Российским квантовым центром создан Центр компетенций НТИ «Квантовые коммуникации» — уникальная научно-образовательная организация России. Вы будете участвовать в разработках квантового компьютера, квантового интернета, квантовых нейронных сетей и искусственного интеллекта. Рискните принять участие в битве века за победу в научно-техническом прогрессе за счет технологий квантового интеллекта и одержите победу вместе с нами!\nУзнать подробности: https://misis.ru/applicants/admission/baccalaureate-and-specialty/faculties/physics/'),
               (3, '«Электроника и наноэлектроника» в НИТУ МИСИС — одно из лучших очных направлений подготовки по специальности в стране. Для него были разработаны уникальные образовательные треки, на которых особое внимание уделяется материаловедению, а также углубленному изучению программирования и английского языка. У нас есть всё для комфортной учебы: современный кампус и инновационные технологии обучения. А благодаря гибкому учебному расписанию студенты направления могут самостоятельно планировать свое время.\nУзнать подробности: https://misis.ru/applicants/admission/baccalaureate-and-specialty/faculties/electro/'),
               (4, 'Хотите научиться создавать новые материалы и внести свой вклад в развитие медицины и технологий? Тогда это направление для вас. Почему в НИТУ МИСИС? Здесь лучшее в стране направление очной подготовки по материаловедению. Богатое историческое наследие и старейшая научная школа, а также лаборатории мирового уровня и современный кампус. У нас собственный подход к организации учебного процесса — вы сможете выбрать профессию после 2 лет фундаментальной подготовки, освоив один из уникальных треков, разработанных совместно с нашими индустриальными партнерами.\nУзнать подробности: https://misis.ru/applicants/admission/baccalaureate-and-specialty/faculties/materialoved/'),
               (5, 'Направление имеет две специализации: "Нанотехнологии и микросистемная техника" и "Наноматериалы"\nУзнать подробности про "Нанотехнологии и микросистемная техника": https://misis.ru/applicants/admission/baccalaureate-and-specialty/faculties/nanotech/\nУзнать подробности про "Наноматериалы": https://misis.ru/applicants/admission/baccalaureate-and-specialty/faculties/nanomaterial/'),
               (6, 'Современная прикладная математика охватывает не только информатику, но всю цифровую экономику. Специалисты в этой области обеспечивают связь между цифровым и материальным миром. Талантливые студенты-математики выбирают наши уникальные очные образовательные треки, аналогов которым нет в России! Наши студенты ежегодно побеждают в хакатонах и соревнованиях по робототехнике. Углубленно изучают английский и осваивают программирование, машинное обучение, нейросети и большие данные под руководством ведущих ученых и практиков не только НИТУ МИСИС, но и МФТИ, Сколтеха и ИТМО.\nУзнать подробности: https://misis.ru/applicants/admission/baccalaureate-and-specialty/faculties/math/'),
               (7, 'Направление имеет три специализации: "Информационные системы и технологии", "Информатика и вычислительная техника" и "Прикладная информатика"\nУзнать подробности про "Информационные системы и технологии": https://misis.ru/applicants/admission/baccalaureate-and-specialty/faculties/informsistemitehno/\nУзнать подробности о "Информатика и вычислительная техника": https://misis.ru/applicants/admission/baccalaureate-and-specialty/faculties/informatikaivt/\nУзнать подробности о "Прикладная информатика": https://misis.ru/applicants/admission/baccalaureate-and-specialty/faculties/prikladnayainformatika/'),
               (8, 'В ходе обучения вы научитесь управлять энергетическими ресурсами предприятия и станете востребованным специалистом в новой, перспективной области — энергоменеджменте. Вы сможете работать в сфере защиты экологии планеты от вредных выбросов. Ваши компетенции помогут повысить энергоэффективность предприятий (прежде всего, минерально-сырьевой отрасли), а значит — сделать их более конкурентоспособными.\nУзнать подробности: https://misis.ru/applicants/admission/baccalaureate-and-specialty/faculties/electroenergetika/'),
               (9, 'Горное дело — профессия, которая возникла еще в древности, и сегодня по-прежнему остается одной из самых востребованных в мире. Парадоксально, но именно в этой сфере существует серьезный дефицит кадров. Вы сможете учиться в современном кампусе и работать на передовом научном оборудовании, с первых курсов будете сотрудничать с работодателями и сами определите свою образовательную траекторию. Вашими конкурентными преимуществами станут навыки применения современных информационных технологий, дистанционных методов зондирования, роботизированных и беспилотных аппаратов. Вы овладеете инженерным искусством, позволяющим чувствовать нашу планету, бережно использовать богатства недр и океанов, а в ближайшем будущем — естественных космических объектов.\nУзнать подробности: https://misis.ru/applicants/admission/specialty/faculties/gornoedelo/'),
               (10, 'Международные рейтинги университетов подтверждают: в НИТУ МИСИС создано одно из лучших направлений очной подготовки в области инжиниринга и технологий в России и в мире. Мы разработали уникальные образовательные треки обучения по программе бакалавриата, у которых нет аналогов. Наши абитуриенты ежегодно создают большой конкурс, а студенты высоко оценивают качество обучения!\nУзнать подробности: https://misis.ru/applicants/admission/baccalaureate-and-specialty/faculties/tehmashin/'),
               (11, 'Хотите сделать успешную карьеру и подарить миру новые возможности и технологии? Поступайте на лучшую в России образовательную программу бакалавриата по металлургии! В ходе обучения Вы станете частью сильнейшего научного сообщества инженеров-металлургов, востребованных в крупнейших индустриальных компаниях. А после выпуска внесете собственный вклад в инновационно-технологическое развитие промышленности и экономики!\nУзнать подробности: https://misis.ru/applicants/admission/baccalaureate-and-specialty/faculties/metall/'),
               (12, 'Направление имеет две специализации: "Экономика" и "Менеджмент". \nУзнать подробности про "Экономика": https://misis.ru/applicants/admission/baccalaureate-and-specialty/faculties/economy/\nУзнать подробности про "Менеджмент": https://misis.ru/applicants/admission/baccalaureate-and-specialty/faculties/management/'),
               (13, 'Современный специалист сферы торговли обладает междисциплинарными знаниями и умениями, системным мышлением, способен к самостоятельному оперативному управлению. Студенты направления овладевают знаниями и практическими навыками, необходимыми для создания логистических цепей, планирования материально-технического обеспечения предприятия, управления товародвижением и другими процессами.\nУзнать подробности: https://misis.ru/applicants/admission/baccalaureate-and-specialty/faculties/torgdelo/'),
               (14, 'Цифровизация глобальных бизнес-процессов нуждается в специалистах, имеющих знания в разных областях: экономики, теории управления и информационных технологий. Пройдя очное обучение по направлению «Бизнес-информатика», вы узнаете, как проводить цифровые инновации во всех секторах экономики, работать над их модернизацией и дальнейшим развитием.\nУзнать подробности: https://misis.ru/applicants/admission/baccalaureate-and-specialty/faculties/bi/')]

# добавляем новую запись в таблицу subjects
cursor.executemany('INSERT INTO specializations_description (id, description) VALUES (?, ?)', description)

# сохраняем изменения в базе данных
conn.commit()

conn.close()