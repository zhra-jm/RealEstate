import sys

from agent import Supervisor
from store import save_to_file
from utils import check_credentials

if check_credentials(sys.argv):
    agent = Supervisor.create_agent()
    save_to_file(Supervisor.agent_data())
else:
    print("wrong cred")