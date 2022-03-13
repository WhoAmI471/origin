from flask import Flask
import utils


app = Flask(__name__)
candidates = utils.load_candidates()

@app.route('/')
def home():
    str = '<pre>'

    for candidate in candidates.values():
        str += f'Имя кандидата - {candidate["name"]} <br>Позиция кандидата {candidate["id"]} <br>Навыки через запятую {candidate["skills"]} <br><br>'

    str += '</pre>'
    return str


@app.route('/candidates/<int:id>')
def profile(id):
    candidate = candidates[id]

    str = f'<img src={candidate["picture"]}></img> <br><br>Имя кандидата - {candidate["name"]} <br>Позиция кандидата {candidate["id"]} <br>Навыки через запятую {candidate["skills"]} <br><br>'

    return str


@app.route('/skill/<skill>')
def search_skill(skill):

    for candidate in candidates.values():
        skills = candidate['skills'].split(', ')
        skills = [x.lower() for x in skills]
        if skill.lower() in skills:
            str = f'Имя кандидата - {candidate["name"]} <br>Позиция кандидата {candidate["id"]} <br>Навыки через запятую {candidate["skills"]} <br><br>'

    return str

    
app.run()