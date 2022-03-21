# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Delete-a-Ticket
from requests import post

from src.faveo_handler.api import FaveoApi


class Delete(FaveoApi):
    def __init__(self, url: str):
        super().__init__(url)

    def delete_ticket(
        self,
        ticket_id: str,
        token: str = None,
        api_key: str = None
    ):
        self._set_data(token, api_key, ticket_id=ticket_id)
        response = post(
            url=f"{self.url}/api/v1/helpdesk/delete",
            headers=self.headers,
            json=self.data
        )
        return response.json()
