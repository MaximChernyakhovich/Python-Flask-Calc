# Проекта
Экспериментальный проект был создан с целью освоения навыков разработки веб-приложений с использованием фреймворка Flask. В его основе лежит легкий веб-калькулятор, разработанный с применением этого инструмента.


# Технологии
- [Python](https://www.python.org/)
- [Flask](https://www.typescriptlang.org/)
- [HTML](https://www.typescriptlang.org/)
- [CSS](https://www.typescriptlang.org/)
Flask==2.2.2
Flask-Bootstrap==3.3.7.1
Flask-WTF==1.1.1
Werkzeug==2.2.2

# Использование

Клонирование репозитория:
```sh
$ git clone https://github.com/MaximChernyakhovich/Python-Flask-Calc.git
```

Запуск с помощью docker:
```sh
$ cd python-flask-calc
$ docker build -t python-flask-calc .
$ docker run -p 5000:5000 python-flask-calc
```

# Разработка

## Требования
Для установки и запуска проекта, необходим [Python](https://www.python.org/).

## Установка зависимостей
Для установки зависимостей, выполните команду:
```sh
$ pip install -r requirements.txt
```

## Запуск
Чтобы запустить сервер для разработки, выполните команду:
```sh
$ python app.py
```
