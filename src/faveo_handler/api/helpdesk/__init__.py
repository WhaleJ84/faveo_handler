from .create import Create
from .read import Read


class Helpdesk(Create, Read):
    def __init__(self, url: str):
        super().__init__(url)
