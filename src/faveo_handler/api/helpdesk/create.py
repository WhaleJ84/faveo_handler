# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Register-a-User
from typing import Union

from requests import post

from src.faveo_handler.api import FaveoApi


class Create(FaveoApi):
    def __init__(self, url: str):
        super().__init__(url)

    def create_ticket(
        self,
        body: str,
        email: str,
        first_name: str,
        helptopic: Union[int, str],
        last_name: str,
        priority: Union[int, str],
        sla: Union[int, str],
        subject: str,
        code: str = None,
        dept: str = None,
        duedate: str = None,
        mobile: str = None,
        phone: str = None,
        user_id: Union[int, str] = None,
        api_key: str = None,
        token: str = None
    ):
        """
        https://github.com/ladybirdweb/faveo-helpdesk/wiki/Create-Ticket

        :param body: Body of the ticket
        :param email: Email of the requester
        :param first_name: First name of the requester
        :param helptopic: Help topic of the ticket
        :param last_name: Last name of the requester
        :param priority: Priority of the ticket
        :param sla: SLA of the ticket
        :param subject: Subject of the ticket
        :param code: Country code of the requestor
        :param dept: ID of the department
        :param duedate: Due date for the ticket
        :param mobile: Mobile number of the requester
        :param phone: Phone number of the requester
        :param user_id: ID of the user
        :param api_key: An alphanumeric code that can be used to authenticate your API calls.
        To make it required login to Admin panel and go to API setting and make it mandatory

        :param token: Token generated for a user
        """
        self._set_data(
            token=token,
            api_key=api_key,
            body=body,
            email=email,
            first_name=first_name,
            helptopic=helptopic,
            last_name=last_name,
            priority=priority,
            sla=sla,
            subject=subject,
            code=code,
            dept=dept,
            duedate=duedate,
            mobile=mobile,
            phone=phone,
            user_id=user_id
        )
        response = post(
            url=f"{self.url}/api/v1/helpdesk/create",
            headers=self.headers,
            json=self.data
        )
        return response.json()
