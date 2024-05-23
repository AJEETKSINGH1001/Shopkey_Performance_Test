from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Wait time between tasks, here between 1 and 5 seconds

    @task
    def load_home_page(self):
        self.client.get("/")

        @task(2)
        def browse_categories(self):
            self.client.get("/?offset=0&category=catalogues")
            self.client.get("/?offset=0&category=deals")

        @task(1)
        def view_product(self):
            self.client.get("/test0106store1a_17159127844310")
            self.client.get("/test0106store1async_13357205729")

        @task(1)
        def add_to_cart(self):
            self.client.post("/cart", {"product_id": "test0106store1a_17159127844310", "quantity": 2})

if __name__ == "__main__":
    import os
    os.system("locust -f locustfile.py --host=https://test0106store1a.goshopkey.com")
