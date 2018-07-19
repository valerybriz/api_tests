'''Read https://docs.locust.io/en/stable/quickstart.html
for examples on how to run the tests'''
from locust import HttpLocust, TaskSet, task
import config as conf

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def login(self):
        self.client.post("/auth/login", json={"username":conf.test_username, "password":conf.test_password})

    @task(2)
    def index(self):
        self.client.get("/git/index")

    @task(1)
    def register(self):
        self.client.get("/git/register")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000

