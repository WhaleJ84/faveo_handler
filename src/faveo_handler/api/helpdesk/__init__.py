from .create import Create
from .read import Read
from .update import Update
from .delete import Delete


class Helpdesk(Create, Read, Update, Delete):
    def __init__(self, url: str):
        super().__init__(url)
