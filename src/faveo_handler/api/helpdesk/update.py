# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Edit-Ticket
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Create-Internal-Note
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Collaborator-Create
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Collaborator-Remove
from typing import Union

from requests import post

from src.faveo_handler.api import FaveoApi


class Update(FaveoApi):
    def __init__(self, url: str):
        super().__init__(url)

    def reply_ticket(
        self,
        ticket_id: Union[int, str],
        reply_content: str,
        token: str = None,
        api_key: str = None,
        ip: str = None
    ):
        """
        https://github.com/ladybirdweb/faveo-helpdesk/wiki/Reply-Ticket

        :param ticket_id: ID of the ticket to reply
        :param reply_content: Body of your reply
        :param token: Token generated for a user
        :param api_key: An alphanumeric code that can be used to authenticate your API calls
        :param ip: IP address of the Customer/location where API call is being made from
        """
        self._set_data(token, api_key, ticket_id=ticket_id, reply_content=reply_content, ip=ip)
        response = post(
            url=f"{self.url}/api/v1/helpdesk/reply",
            headers=self.headers,
            json=self.data
        )
        return response.json()
