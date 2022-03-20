from requests import get, post


class FaveoHandler:
    def __init__(self, url: str):
        """
        :param url: Base URL to the Faveo instance. e.g. `https://faveo.example.com'
        """
        self.url = url.strip("/")
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        self.data = {
            "token": None
        }

    def authenticate(self, username: str, password: str):
        response = post(
            url=f"{self.url}/api/v1/authenticate",
            headers=self.headers,
            json={
                "username": username,
                "password": password
            }
        )
        self.data["token"] = response.json()["token"]
        return self.data["token"]

    def get_tickets(self):
        response = get(
            url=f"{self.url}/api/v1/helpdesk/tickets",
            headers=self.headers,
            json=self.data
        )
        return response.json()
