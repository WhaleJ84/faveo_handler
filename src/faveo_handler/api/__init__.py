class FaveoApi:
    def __init__(self, url: str, api_key: str = None):
        """
        :param url: Base URL to the Faveo instance. e.g. `https://faveo.example.com'
        :param api_key: An alphanumeric code that can be used to authenticate your API calls.
        To make it required login to Admin panel and go to API setting and make it mandatory
        """
        self.url = url.strip("/")
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        self._data = {
            "token": None,
            "api_key": api_key,
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
            try:
                token = self.data["token"]
            except KeyError:
                pass
        self.data["token"] = token
        return self.data["token"]

    def _set_api_key(self, api_key: str = None):
        # API key does not want to be wiped every time the data is cleared
        # This will keep the original value unless stated otherwise
        if not api_key:
            try:
                api_key = self.data["api_key"]
            except KeyError:
                pass
        self.data["api_key"] = api_key
        return self.data["api_key"]

    def _remove_none_values_from_data(self):
        for key, value in list(self.data.items()):
            if value is None:
                del self.data[key]
        return self.data

    def _set_data(
        self,
        token: str = None,
        api_key: str = None
    ):
        self._set_token(token)
        self._set_api_key(api_key)
        self._remove_none_values_from_data()
        return self.data
