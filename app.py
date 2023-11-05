from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import *
from wtforms.validators import DataRequired

# Импорт необходимых библиотек и создание экземпляра Flask
app = Flask(__name__)
bootstrap = Bootstrap(app)

# Настройка секретного ключа для защиты форм
app.config['SECRET_KEY'] = 'secret'

# Определите путь к каталогу со статическими файлами
app.config['STATIC_FOLDER'] = 'static'

# Определение формы для ввода выражения в калькуляторе
class CalculatorForm(FlaskForm):
    expression = StringField('Enter an expression')
    submit = SubmitField('Calculate')

# Разрешите обслуживание статических файлов
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.config['STATIC_FOLDER'], filename)

# Основной маршрут для калькулятора
@app.route('/', methods=['GET', 'POST'])
def calculator():
    # Получение истории вычислений из сессии
    history = session.setdefault('history', [])
    result = ''

    # Обработка запроса на вычисление выражения
    if request.method == 'POST':
        # Получение выражения из формы
        expression = request.form['expression']
        try:
            # Вычисление результата выражения и его преобразование в строку
            result = str(eval(expression))
            # Проверка на деление на ноль
            if '/ 0' in expression or '/0' in expression:
                raise ZeroDivisionError
        except (SyntaxError, ValueError):
            # Обработка ошибок в выражении
            result = 'Ошибка в выражении'
        except ZeroDivisionError:
            # Обработка деления на ноль
            result = 'Деление на ноль запрещено!'
        else:
            # Генерация порядкового номера для записи в историю
            order = len(history) + 1
            # Создание элемента истории вычислений
            history_item = {'expression': expression[:50], 'result': result[:50], 'order': order}
            # Добавление элемента в историю, если его нет там
            if expression[:50] not in history:
                history.insert(0, history_item)
            # Ограничение размера истории до 20 элементов
            history = history[:20]
            # Обновление истории в сессии с сортировкой по порядковому номеру
            session['history'] = sorted(history, key=lambda x: x.get('order', 0), reverse=True)

    # Отправка результата и истории в шаблон для отображения
    return render_template('calculator.html', result=result, history=session['history'])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)