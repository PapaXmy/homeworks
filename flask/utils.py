import json

def load_json() -> list[dict]:
    with open('candidates.json', 'r') as file:
        candidats = json.load(file)
        return candidats

def format_candidates(candidats: list[dict]) -> str:
    result = '<pre>'

    for candidate in candidats:
        result += f'''
                {candidate['name']}\n
                {candidate['position']}\n
                {candidate['skills']}
            '''
    result += '</pre>'
    return result

def get_all_candidates() -> list[dict]:
    return load_json()

def get_candidate_by_id(uid: int) -> dict | None:
    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate['id'] == uid:
            return candidate
    return None

def get_candidate_skill(skill: str) -> list[dict]:
    candidates = get_all_candidates()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result
