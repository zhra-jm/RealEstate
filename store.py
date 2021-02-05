import json


def save_to_file(data):
    with open('agent.jason', 'w') as f:
        f.writelines(json.dumps(data))


def load_data():
    with open('agent.jason', 'r') as f:
        agents = f.read()
    return json.loads(agents)

