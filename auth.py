from agent import Agent, Supervisor
from store import load_data

agents_data = load_data()
_ = [Agent(**d) for d in agents_data]
agent = None
while agent is None:
    username = input("Enter ur username: ")
    agent = Supervisor.search(username)
password = input("Enter ue password: ")
if agent.check_password(password):
    print("WLC")
else:
    print("wrong pass")
