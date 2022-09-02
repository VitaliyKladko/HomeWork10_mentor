from flask import Flask
from utils import load_candidates, get_all, get_by_pk, get_by_skill

FILENAME = 'candidates.json'
data = get_all(load_candidates(FILENAME))

app = Flask(__name__)

@app.route('/')
def index():
    str = '<pre>' # <pre> позволяет сохранить форматирование внутри текста
    for i in data:
        str += f'{i} \n'
    str += '</pre>' # <pre> позволяет сохранить форматирование внутри текста
    return str

@app.route('/candidates/<int:pk>/')
def get_user(pk):
    user = get_by_pk(pk, data)
    if user:
        str = f'<img src = "{user.picture}">'
        str += f'<pre> {user} </pre>'
    else:
        str = 'Candidate NOT FOUND'
    return str

@app.route('/skills/<skill>')
def get_user_skill(skill):
    skill = skill.lower()
    user = get_by_skill(skill, data)
    if user:
        str = '<pre>'
        for item in user:
            str += f'{item} \n'
        str += '</pre>'
    else:
        str = 'SKILL NOT FOUND'
    return str

if __name__ == '__main__':
    app.run(port=5000)