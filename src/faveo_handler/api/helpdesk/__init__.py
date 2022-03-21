from .create import Create
from .read import Read
from .delete import Delete


class Helpdesk(Create, Read, Delete):
    def __init__(self, url: str):
        super().__init__(url)
