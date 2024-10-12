from database import db
from database import models


def load_main_questions():
	session = db.SessionLocal()
	questions = [
		models.MainQuestion(
			id=1,
			short_name='Вход-макет',
			content='Впереди тебя ждут интересные вопросы, загадки и задачи'
					'про университет, решая которые ты будешь узнавать все '
					'больше и больше об этом месте. Все вопросы поделены по '
					'блокам, каждый из которых можно будет открыть после конца '
					'предыдущего, решив контрольную задачку, которую ты '
					'сможешь получить, отсканировав QR-код в одном из интересных '
					'мест университета. Не волнуйся, мы обязательно подскажем тебе, '
					'где найти QR и как решить задачку. Удачи в прохождении! '
					'Чтобы запустить квест нажми кнопку "Начать"',
		),
		models.MainQuestion(
			id=2,
			short_name='Аудитории',
			content='Следующий вопрос откроется тебе, когда ты отправишь сюда '
					'правильный ответ на задачку, которую ты можешь найти по '
					'QR-коду около места, номер которого совпадает с самой '
					'крутой бургерной в городе.',
			answer='юг',
			right_response='Отлично! в загадке были зашифрованы 4 стороны света, отображенные с помощью стран.'
						   ' И у нас в университете есть 4 аудитории с названиями как у сторон света!'
						   ' Недалеко от тебя находятся диваны, можешь присесть и ответить на следующие'
						   ' вопросы в удобном положении)',
			wrong_response='Неверно( правильный ответ - юг. в загадке были зашифрованы 4 стороны света, отображенные '
						   'с помощью стран. И у нас в университете есть 4 аудитории с названиями как у сторон света!'
						   'недалеко от тебя находятся диваны, можешь присесть и ответить'
						   ' на следующие вопросы в удобном положении) '
		),
		models.MainQuestion(
			id=3,
			short_name='Читалка',
			content='Следующий вопрос откроется тебе, когда ты отправишь сюда '
					'правильный ответ на задачку, которую ты можешь найти по QR-коду '
					'в месте, где нужно быть очень тихим и внимательным!',
			answer='библиотека',
			right_response='Отлично! Сейчас ты находишься в читальном зале, это очень уютное и доброе место.'
						   ' Сейчас самое время, чтобы присесть, отдохнуть и ответить на несколько интересных вопросов',
			wrong_response='Неверно( правильный ответ - библиотека. Сейчас ты находишься в читальном зале,'
						   ' это очень уютное и доброе место. Сейчас самое время, чтобы присесть, отдохнуть'
						   ' и ответить на несколько интересных вопросов!'
		),
		models.MainQuestion(
			id=4,
			short_name='Matrix',
			content='Следующий вопрос откроется тебе, когда ты отправишь сюда правильный '
					'ответ на задачку, которую ты можешь найти по QR-коду в месте, где '
					'можно провести время с пользой для здоровья!',
			answer='матрица',
			right_response='Отлично! сейчас вы как раз находитесь в столовой под названием matrix(матрица).'
						   ' Между прочим, одно из моих любимых мест в университете!',
			wrong_response='Неверно( правильный ответ - матрица. Сейчас вы как раз находитесь в столовой под'
						   ' названием matrix(матрица). между прочим, одно из моих любимых мест в университете!'
		),
		models.MainQuestion(
			id=5,
			short_name='Чилл зона-лестница',
			content='Следующий вопрос откроется тебе, когда ты отправишь сюда правильный '
					'ответ на задачку, которую ты можешь найти по QR-коду в месте, '
					'где наконец можно отдохнуть и посидеть. Кстати, оно находится '
					'на 2 этажа выше чем ты сейчас)',
			answer='конец',
			right_response='Верно! да, к сожалению, это уже конец нашей интерактивной экскурсии. Но не расстраивайся,'
						   ' впереди тебя ждет еще несколько интересных вопросов про сам город Иннополис!',
			wrong_response='Неверно( правильный ответ - конец. да, к сожалению, это уже конец нашей интерактивной'
						   ' экскурсии. Но не расстраивайся, впереди тебя ждет еще несколько интересных вопросов'
						   ' про сам город Иннополис!'
		)
	]
	session.query(models.MainQuestion).delete()  # Очищаем таблицу
	session.add_all(questions)
	session.commit()


def get_all():
	session = db.SessionLocal()
	query = session.query(models.MainQuestion)

	data = query.filter().all()
	return data


def get_main_question(main_q_id: int):
	session = db.SessionLocal()
	query = session.query(models.MainQuestion)
	return query.filter(models.MainQuestion.id == main_q_id).one_or_none()


def count_rows():
	session = db.SessionLocal()
	query = session.query(models.MainQuestion)
	return query.count()
