'''Read https://docs.locust.io/en/stable/quickstart.html
for examples on how to run the tests'''
from locust import HttpLocust, TaskSet, task

class HelloBehavior(TaskSet):
    @task
    def helloworld(self):
        self.client.get("/helloworld")


class WebsiteHello(HttpLocust):
    """
    Locust user class that does requests to the locust web server running on localhost
    """
    task_set = HelloBehavior
    min_wait = 5000
    max_wait = 9000