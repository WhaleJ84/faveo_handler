from src.faveo_handler.api.authenticate import Authenticate
from src.faveo_handler.api.helpdesk import Helpdesk


class FaveoHandler(Authenticate, Helpdesk):
    def __init__(self, url: str):
        super().__init__(url)
