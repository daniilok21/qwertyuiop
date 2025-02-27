import json
from flask import Flask, url_for, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/', defaults={'title': None})
@app.route('/index', defaults={'title': None})
@app.route('/index/<title>')
def index(title):
    param = {}
    param['title'] = title
    return render_template('index.html', **param)


@app.route('/list_prof/')
@app.route('/list_prof/<prof>')
def list_prof(prof=''):
    professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                   'инженер по терраформированию', 'климатолог',
                   'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                   'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                   'штурман', 'пилот дронов']
    param = {}
    param['title'] = 'Список профессий'
    param['prof'] = prof
    param['professions'] = professions
    return render_template('list_of_prof.html', **param)


@app.route('/training/<prof>')
def training(prof=''):
    param = {}
    param['title'] = 'Тренировки в полёте'
    param['prof'] = prof
    return render_template('list_of_prof.html', **param)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
