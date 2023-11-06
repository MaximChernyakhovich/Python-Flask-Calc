# О проекте

Данный проект является тестовым и был создан с целью изучения фреймворка Flask. Это простое веб-приложение-калькулятор, разработанное для практики основных принципов работы с Flask.

### Используемые технологии
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [HTML](https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/HTML_basics)
- [CSS](https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/CSS_basics)


## Используемые версии библиотек:

- Flask==2.2.2
- Flask-Bootstrap==3.3.7.1
- Flask-WTF==1.1.1
- Werkzeug==2.2.2


## Инструкции по использованию
### Клонирование репозитория:
```
$ git clone https://github.com/MaximChernyakhovich/Python-Flask-Calc.git
```
### Запуск с помощью Docker:
```
$ cd python-flask-calc
$ docker build -t python-flask-calc .
$ docker run -p 5000:5000 python-flask-calc
```

## Разработка
### Требования
Для установки и запуска проекта необходим Python.

### Установка зависимостей
Для установки зависимостей выполните следующую команду:

```
$ pip install -r requirements.txt
```

### Запуск
Чтобы запустить сервер для разработки, выполните команду:

```
$ python app.py
```
