# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Check-URL
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Opened-Tickets
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Unassigned-Tickets
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Closed-Tickets
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Get-all-Agents
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Get-All-Teams
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Search-Customers
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Customers---Specific-information
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Customer
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Ticket-Threads
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Get-Help-Topics
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Get-SLA-Plans
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Get-Priorities
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Get-Departments
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Get-Inbox
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Get-Trash
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Get-Tickets-By-Agent
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Get-Tickets-By-User
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Collaborator-Search
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Collaborator-Fetch-Associated-with-Ticket
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Dependency-API
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Get-Specific-Ticket-Details
# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Faveo-tickets-API-with-filters-and-order
from requests import get

from src.faveo_handler.api import FaveoApi


class Read(FaveoApi):
    def __init__(self, url: str):
        super().__init__(url)

    def get_tickets(self, token: str = None, api_key: str = None):
        """
        https://github.com/ladybirdweb/faveo-helpdesk/wiki/Get-Tickets

        :param token: Token generated for a user
        :param api_key: An alphanumeric code that can be used to authenticate your API calls
        """
        self._set_data(token=token, api_key=api_key)
        response = get(
            url=f"{self.url}/api/v1/helpdesk/tickets",
            headers=self.headers,
            json=self.data
        )
        return response.json()
