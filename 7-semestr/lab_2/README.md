Необходимо построить такую базу данных, в которой хранится информация как о
технических характеристиках маршрутов, содержащаяся в расписании, так и
информация о наличии мест на рейсы, и информация о пассажирах, купивших билеты
на определенный рейс.

Таблицы:

- город (название города),
- маршрут (номер маршрута, откуда, куда),
- расписание маршрута (маршрут, время отправления, время прибытия),
- модель автобуса (название модели, количество мест),
- автобус (модель автобуса, номер автобуса),
- рейс (расписание маршрута, автобус, дата отправления, цена),
- билет (номер места, рейс, ФИО)

Схема:

<img src="schema.png" />
