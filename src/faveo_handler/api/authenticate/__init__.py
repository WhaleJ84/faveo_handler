from requests import get, post

from src.faveo_handler.api import FaveoApi


class Authenticate(FaveoApi):
    def __init__(self, url: str):
        super().__init__(url)

    def authenticate(self, username: str, password: str, api_key: str = None):
        """
        https://github.com/ladybirdweb/faveo-helpdesk/wiki/Access-and-Authentication

        :param username: Username of the user
        :param password: Password of the user
        :param api_key: An alphanumeric code that can be used to authenticate your API calls.
        To make it required login to Admin panel and go to API setting and make it mandatory
        """
        self._set_data(api_key=api_key)
        self.data["username"] = username
        self.data["password"] = password
        response = post(
            url=f"{self.url}/api/v1/authenticate",
            headers=self.headers,
            json=self.data
        )
        self.data["token"] = response.json()["token"]
        self.data.pop("username")
        self.data.pop("password")
        return self.data["token"]

    def get_authenticated_user(self, api_key: str = None, token: str = None):
        """
        https://github.com/ladybirdweb/faveo-helpdesk/wiki/Get-Authenticated-User

        :param api_key: An alphanumeric code that can be used to authenticate your API calls.
        To make it required login to Admin panel and go to API setting and make it mandatory

        :param token: Token generated for a user
        """
        self._set_data(api_key=api_key, token=token)
        response = get(
            url=f"{self.url}/api/v1/authenticate/user",
            headers=self.headers,
            json=self.data
        )
        return response.json()
