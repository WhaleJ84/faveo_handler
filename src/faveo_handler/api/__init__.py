class FaveoApi:
    def __init__(self, url: str):
        """
        :param url: Base URL to the Faveo instance. e.g. `https://faveo.example.com'
        """
        self.url = url.strip("/")
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        self._data = {
            "token": None,
            "api_key": None,
        }
        self.data = self._data

    def _set_url(self, url: str = None):
        self.url = url.strip("/")
        return self.url

    def _set_headers(self, headers: dict = None):
        self.headers = headers
        return self.headers

    def _set_token(self, token: str = None):
        # Token does not necessarily want to be wiped every time the data is cleared
        # This will keep the original value unless stated otherwise
        if not token:
            token = self.data["token"]
        self.data["token"] = token
        return self.data["token"]

    def _set_api_key(self, api_key: str = None):
        # API key does not want to be wiped every time the data is cleared
        # This will keep the original value unless stated otherwise
        if not api_key:
            api_key = self.data["api_key"]
        self.data["api_key"] = api_key
        return self.data["api_key"]

    def _set_data(
        self,
        token: str = None,
        api_key: str = None
    ):
        self._set_token(token)
        self._set_api_key(api_key)
        return self.data
