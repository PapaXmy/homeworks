from flask import Flask
from utils import get_all_candidates, format_candidates, get_candidate_by_id, get_candidate_skill

app = Flask(__name__)


@app.route('/')
def page_maine():
    candidats: list[dict] = get_all_candidates()
    result: str = format_candidates(candidats)

    result += '</pre>'
    return result


@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    candidats: dict = get_candidate_by_id(uid)
    result = f'<img src="{candidats["picture"]}">'
    result += format_candidates([candidats])
    return result


@app.route('/skills/<skill>')
def page_skill(skill):
    skill_lower = skill.lower()
    candidats: list[dict] = get_candidate_skill(skill_lower)
    result = format_candidates(candidats)
    return result


app.run()
