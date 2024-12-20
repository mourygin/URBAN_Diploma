# Программа сайта интернет-магазина на языке Python с использованием фрэймворка Django.
Настоящий проект выполнен в качестве дипломной работы по завершению курса "Python-разработчик". В проекте реализована программа интернет-магазина игрушек. Текущая версия - pre-BETA.
Программа написана на языке Python с использованием фрэймворка Django.
## Технологии:
<a href="https://www.python.org/"><b>Python</b></a><br>
<a href="https://www.djangoproject.com/"><b>Django framework</b></a><br>
<a href="https://www.sqlite.org/"><b>SQLite database</b></a>
## Использование:
Предварительно на компьютере должен быть установлен Python. Программа свободно распространяемая. Официальный сайт - <a href="https://www.python.org/">python.org</a><br>
Необходимые для работы программы библиотеки указаны в файле requirements.txt<br>
Все их можно установить с помощью команды <b>pip install -r requirements.txt</b><br>
Далее следует войти в каталог shop и запустить web-сервер командой <b>python manage.py runserver</b><br>
Перейдите по появившейся ссылке <i>http://127.0.0.1:8000/</i><br>
# Введение.
В современном мире интернет играет огромную роль в жизни людей. Он предоставляет доступ к огромному количеству информации, позволяет общаться с друзьями и знакомыми, а также совершать покупки онлайн. Интернет-магазины стали неотъемлемой частью нашей повседневной жизни, позволяя нам покупать товары и услуги, не выходя из дома.

В этом разделе мы рассмотрим возможность разработки программ сайтов интернет-магазинов на языке Python с использованием фреймворка Django. Мы обсудим основные преимущества и недостатки использования этих технологий, а также определим цели и задачи нашего исследования.
# Обоснование выбора темы.
Как уже было сказано выше интернет-магазины играют значимую роль в современной экономике. Так годовой товарооборот российских интернет-магазинов в 2023 году составил около 6,4 трлн рублей, а доля электронной коммерции в общем объёме розничных продаж достигла 13,8%.

В соответствии со столь высокой значимостью данного вида экономической активности высока и потребность рынка в программном обеспечении, предоставляющим возможность проведения электронной коммерции, в том числе и интернет-магазинов.

Разработка представляемой программы дает возможность развития и совершенствования своих профессиональных навыков в сфере создания web-приложений. 

Использование высокоуровневого языка программирования Python в сочетании со специализированным фреймворком Django позволяют повысить имеющийся личный опыт создания web-приложений с помощью таких CMS (Content management system) как Joomla и WordPress в сторону построения более гибких и разноплановых систем, поддающихся достижения большего соответствия достигнутого результата техническому заданию.
# Цели и задачи.
Задачей настоящей работы является разработка программы web-сайта, реализующего основные функции интернет-магазина. Данная задача решается с использованием языка Python в сочетании с фрэймворком Django и базой данных на основе «движка» (database engine) SQLite.

Решение указанной задачи преследует следующие цели:

•	закрепить знания и навыки, полученные в ходе обучения;

•	представить работу в качестве дипломного проекта и успешно его защитить.
# Основные понятия и определения.
•	<b>Web-сайт</b> – одна или несколько логически связанных между собой веб-страниц; также место расположения контента сервера. Обычно сайт в Интернете представляет собой массив связанных данных, имеющий уникальный адрес и воспринимаемый пользователями как единое целое. Доступ к web-сайту происходит по протоколу HTTP или HTTPS.

•	<b>Интернет-магазин</b> – сайт, торгующий товарами посредством сети Интернет. Позволяет пользователям онлайн, в своём браузере или через мобильное приложение, сформировать заказ на покупку, выбрать способ оплаты и доставки заказа, оплатить заказ. При этом продажа товаров осуществляется дистанционным способом и она накладывает ограничения на продаваемые товары. Так, в некоторых странах имеется запрет на интернет-торговлю алкоголем, оружием, ювелирными изделиями и другими товарами. К примеру, в России запрещена дистанционная продажа алкоголя и других товаров, свободная реализация которых ограничена. Типичный интернет-магазин позволяет клиенту просматривать ассортимент продуктов, просматривать фотографии или иные изображения продуктов, а также информацию о технических характеристиках продукта и ценах.

•	<b>Фрэймворк</b> – программное обеспечение, облегчающее разработку и объединение разных компонентов большого программного проекта. Фреймворк отличается от понятия библиотеки тем, что последняя может быть использована в программном продукте просто как набор подпрограмм похожей функциональности, не влияя на архитектуру программного продукта и не накладывая на неё никаких ограничений. В то время как фреймворк диктует правила построения архитектуры приложения. Веб-фреймворк - фреймворк, предназначенный для создания динамических веб-сайтов. Он упрощает разработку и избавляет от необходимости написания рутинного кода. Многие фреймворки упрощают доступ к базам данных, разработку интерфейса, и также уменьшают дублирование кода.

•	<b>База данных</b> – организованная в соответствии с определёнными правилами совокупность данных, характеризующая актуальное состояние некоторой предметной области и используемая для удовлетворения информационных потребностей пользователей. База данных обладает следующими отличительными признаками:
- БД хранится и обрабатывается в вычислительной системе;
- Данные в БД логически структурированы с целью обеспечения возможности их эффективного поиска и обработки в вычислительной системе;
- БД включает схему, или метаданные, описывающие логическую структуру БД.

•	<b>Схема данных</b> – включает в себя описание содержания, структуры и ограничений целостности, используемые для создания и поддержки базы данных, её структура, описанная на формальном языке. В реляционных базах данных схема определяет таблицы, поля в каждой таблице (с указанием их названия, типа, обязательности), и ограничения целостности. Хотя схема определена на языке базы данных в виде текста, термин часто используется для обозначения графического представления структуры базы данных.
# Подходы к разработке и структура приложения.
## Стиль и художественный дизайн сайта.

Каждый web-сайт, предназначенный для широкого круга пользователей, должен иметь дизайн, соответствующий своей аудитории. В частности, это относится к интернет-магазинам. Так как предполагаемыми посетителями нашего магазина будут являться не сами пользователи его товаров – дети, а их родители, в качестве базового, фонового был выбран нежно-абрикосовый цвет, соответствующий «эмоциональной окраске» родительских чувств.

Использование ярких агрессивных цветов было сведено к минимуму. Из ярких был использован лишь красный цвет заголовков страниц, так как он находится в близкой гамме.

Стилистика изображений выдержана в стиле иллюстраций детских книг середины ХХ века, что рассчитано на пробуждение детских воспоминаний посетителей сайта.

## Схема данных.

Структура данных формируется фреймворком Django двумя путями – первая часть таблиц, являющихся служебными, образуется при подключении Django к базе данных. Ограничимся их перечислением с краткими комментариями:

•	django_migrations – хранение информации о миграциях моделей;<br>
•	sqlite_sequence – внутренняя таблица, необходимая для реализации AUTOINCREMENT. Для каждой пользовательской таблицы использующей инкремент, соответствует строка таблицы;<br>
•	auth_group_permissions – таблица связи M2M между разрешениями и группами;<br>
•	auth_user_groups –  таблица связи M2M между пользователями и группами;<br>
•	auth_user_user_permissions – таблица связи M2M между разрешениями и пользователями;<br>
•	django_admin_log –логирование транзакций, активированных администратором;<br>
•	django_content_type – хранение данных о приложениях и моделях;<br>
•	auth_permission –  хранение информации о пользовательских разрешениях;<br>
•	auth_group – хранение информации о группах (ролях) пользователей;<br>
•	auth_user – таблица пользователей БД;<br>
•	django_session – хранение информации о сессиях;<br>

Вторая часть таблиц образуется и модифицируется при миграциях Django-моделей. Именно эти таблицы образуют предметную схему данных. Попытаемся описать ее более детально.<br>

Имена этих таблиц составляются системой автоматически из имени Django-приложения (в нашем случае – toy_department) и имени модели. Например - toy_department_buyer или toy_department_toy. Для таблиц, осуществляющих связь «многие-ко-многим», к имени приложения и имени модели добавляется еще и имя поля связи. Например - toy_department_toy_toy_cat.

![DB_schema](https://github.com/user-attachments/assets/a67a1985-2c3a-4c6c-b39a-182353b14e65)

Рис.1 Схема данных интернет-магазина.

На рисунке 1 представлена схема данных интернет-магазина в его начальной версии. Из схемы видно что основная информация проекта содержится в таблицах категорий товара (toy_department_category), наименований товара (toy_department_toy) и таблице покупателей (toy_department_buyer).

Таблица toy_department_toy_toy_cat является таблицей связи «многие-ко-многим» между категориями и товарами. Это связано со спецификой магазина, где некоторые товары могут быть отнесены более чем к одной категории (например – какая-то игрушка может присутствовать как в категории «Для мальчишек», так и в категории «Для девчонок»). В большинстве интернет-магазинов каждый товар относится к какой-либо категории однозначно и необходимость в такой таблице отсутствует.

Таблица toy_department_basket, содержащая информацию о покупательских «Корзинах», графически также похожая на связь «многие-ко-многим», таковой не является, а отражает реальную сущность «покупок». Здесь недостаточно, как в случае исключительно связной таблицы, лишь двух полей с идентификаторами связываемых сущностей. На самом деле дополнительные поля, присутствующие в текущей версии, служат лишь для удобства вывода информации на страницу «Корзина». Однако, в любом случае, при появлении в проекте функционала оплаты и доставки, эта таблица дополнится соответствующими полями.

Таблица toy_department_action, содержащая информацию о проводимых в магазине акциях, стоит как-бы особняком от остальных элементов схемы. Это объясняется тем, что акции носят разовый характер и не вписаны в основной технологический процесс магазина.

Рассмотрим структуру перечисленных таблиц детально, с описанием полей.

<ins>Таблица категорий товаров (toy_department_category):</ins><br>
•	id – первичный ключ, идентификатор категории (в описании модели отсутствует, создается фреймворком)<br>
•	cat_name – текстовое поле, наименование категории<br>

В системе прописаны 4 категории товаров: игрушки для мальчиков («Мальчишкам…»), игрушки для девочек («Девчонкам…»), игрушки для животных («Питомцам…») и подарочные игрушки («_presents») вручаемые во время акций и имеющие нулевую цену.

<ins>Таблица товаров (toy_department_toy):</ins><br>
•	id – первичный ключ, идентификатор товара (в описании модели отсутствует, создается фреймворком);<br>
•	title – текстовое поле, наименование товара;<br>
•	articul – текстовое поле, артикул товара в произвольном формате;<br>
•	cost – числовое (float) поле, цена товара;<br>
•	actual_cost – числовое (float) поле, цена товара с учетом скидок, действующих на момент продажи;<br>
•	weight – числовое (float) поле, вес единицы товара;<br>
•	description – текстовое поле, описание товара;<br>
•	in_stock – числовое (integer) поле, доступное количество единиц товара;<br>
•	picture_min – текстовое поле, имя файла миниатюрного изображения товара. Совместимые форматы (PNG, JPG);<br>
•	picture_max – текстовое поле, имя файла детального, возможно анимированного, изображения товара. Совместимые форматы (PNG, JPG, GIF, MP4);<br>
•	toy_cat – категория товара (связь «многие-ко-многим»)<br>

<ins>Таблица покупателей (toy_department_buyer):</ins><br>
•	id – первичный ключ, идентификатор покупателя (в описании модели отсутствует, создается фреймворком);<br>
•	name – текстовое поле, имя покупателя в системе;<br>
•	balance – числовое (float) поле, баланс (внесенная в систему предоплата) покупателя;<br>
•	age – числовое (integer) поле, возраст покупателя;<br>
•	psw – текстовое поле, хэш-функция (md5) пароля;<br>
•	phone_nr – текстовое поле, номер телефона покупателя;<br>
•	address – текстовое поле, адрес покупателя;<br>

<ins>Таблица покупательских корзин (toy_department_basket):</ins><br>
•	id – первичный ключ, идентификатор покупки (в описании модели отсутствует, создается фреймворком);<br>
•	buyer_id_id – внешний ключ, идентифицирующий покупателя;<br>
•	toy_id_id – внешний ключ, идентифицирующий товар;<br>
•	toy_name – текстовое поле, наименование товара;<br>
•	toy_descr – текстовое поле, описание товара;<br>

Два последних поля не вполне соответствуют принципам нормализации базы, но несколько облегчают вывод информации на страницу.

<ins>Таблица торговых акций (toy_department_action):</ins><br>
•	id – первичный ключ, идентификатор акции (в описании модели отсутствует, создается фреймворком);<br>
•	title – текстовое поле, наименование акции;<br>
•	text – текстовое поле, описание акции;<br>
•	first_date – поле даты, начало акции;<br>
•	last_date – поле даты, окончание акции;<br>
•	picture_fn – текстовое поле, имя файла картинки, иллюстрирующей акцию. Совместимые форматы (PNG, JPG);<br>
•	published – логическое поле, разрешающее публикацию акции;<br>
•	presents – логическое поле, указывающее на вручение подарков в течение акции;<br>
•	discont – числовое (float) поле, указывающее на размер скидок в течение акции;<br>
•	actual – логическое поле, указывающее на актуальность акции на текущую дату.<br>

В дальнейшем, при обсуждении развития проекта, мы поговорим о возможных путях совершенствования данной схемы.

## Файловая структура проекта.

![FileStructure](https://github.com/user-attachments/assets/bae0c834-4a88-4047-9e9c-11a23aa831c1)

