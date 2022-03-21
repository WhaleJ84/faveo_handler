from typing import Union

from requests import post

from src.faveo_handler.api import FaveoApi


class Delete(FaveoApi):
    def __init__(self, url: str):
        super().__init__(url)

    def delete_ticket(
        self,
        ticket_id: Union[int, str],
        token: str = None,
        api_key: str = None
    ):
        """
        https://github.com/ladybirdweb/faveo-helpdesk/wiki/Delete-a-Ticket

        :param ticket_id: ID of the ticket want to delete
        :param token: An alphanumeric code that can be used to authenticate your API calls
        :param api_key: Token generated for a user
        """
        self._set_data(token, api_key, ticket_id=ticket_id)
        response = post(
            url=f"{self.url}/api/v1/helpdesk/delete",
            headers=self.headers,
            json=self.data
        )
        return response.json()
