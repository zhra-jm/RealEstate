from decorators import check_access


class BaseUser:
    def __init__(self, username, password, first_name, last_name, email, **kwargs):
        super().__init__(**kwargs)
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @classmethod
    def prompt(cls):
        username = input("username: ")
        password = input("password: ")
        first_name = input("first name: ")
        last_name = input("last name: ")
        email = input("email: ")
        return {
            'username': username, 'password': password, 'first_name': first_name,
            'last_name': last_name, 'email': email
        }


class Supervisor(BaseUser):
    agents_list = list()
    properties_list = dict()
    deals_list = list()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def create_agent():
        agent_data = Agent.prompt()
        agent = Agent(**agent_data)
        return agent

    @classmethod
    def agent_data(cls):
        tmp = []
        for agent in cls.agents_list:
            tmp.append(agent.serializer())
            return tmp

    @classmethod
    def search(cls, username):
        for agent in cls.agents_list:
            if agent.username == username:
                return agent
        return None


class Agent(BaseUser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Supervisor.agents_list.append(self)
        self.__has_access = False
        self.properties_list = list()
        self.deals_list = list()

    def create_property(self, **kwargs):
        # create property
        instance = None
        self.properties_list.append(instance)
        Supervisor.properties_list[self.username].append(instance)

    @classmethod
    def prompt(cls):
        return BaseUser.prompt()

    def serializer(self):
        data = self.__dict__
        data.pop("properties_list")
        data.pop("deals_list")
        data.pop("__has_access", None)
        return data

    def check_password(self, password):
        check = bool(self.password == password)
        if check:
            self.__has_access = True
        return check

    def has_access(self):
        return self.__has_access

    @check_access
    def create_deal(self):
        pass
