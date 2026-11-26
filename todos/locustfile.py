from locust import HttpUser, task, between

class FastAPIUser(HttpUser):
    wait_time = between(0.01, 0.02)  # время между запросами (10-20 мс)

    @task
    def root(self):
        self.client.get("/")
