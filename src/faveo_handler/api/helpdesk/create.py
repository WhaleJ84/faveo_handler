# https://github.com/ladybirdweb/faveo-helpdesk/wiki/Register-a-User
from requests import post

from src.faveo_handler.api import FaveoApi


class Create(FaveoApi):
    def __init__(self, url: str):
        super().__init__(url)
        self._data = {
            "body": None,
            "code": None,
            "dept": None,
            "duedate": None,
            "email": None,
            "first_name": None,
            "helptopic": None,
            "last_name": None,
            "mobile": None,
            "phone": None,
            "priority": None,
            "sla": None,
            "subject": None,
            "user_id": None,
        }
        self.data.update(self._data)

    def _set_body(self, body: str = None):
        self.data["body"] = body
        return self.data["body"]

    def _set_code(self, code: str = None):
        self.data["code"] = code
        return self.data["code"]

    def _set_dept(self, dept: str = None):
        self.data["dept"] = dept
        return self.data["dept"]

    def _set_deudate(self, duedate: str = None):
        self.data["duedate"] = duedate
        return self.data["duedate"]

    def _set_email(self, email: str = None):
        self.data["email"] = email
        return self.data["email"]

    def _set_first_name(self, first_name: str = None):
        self.data["first_name"] = first_name
        return self.data["first_name"]

    def _set_helptopic(self, helptopic: str = None):
        self.data["helptopic"] = helptopic
        return self.data["helptopic"]

    def _set_last_name(self, last_name: str = None):
        self.data["last_name"] = last_name
        return self.data["last_name"]

    def _set_mobile(self, mobile: str = None):
        self.data["mobile"] = mobile
        return self.data["mobile"]

    def _set_phone(self, phone: str = None):
        self.data["phone"] = phone
        return self.data["phone"]

    def _set_priority(self, priority: str = None):
        self.data["priority"] = priority
        return self.data["priority"]

    def _set_sla(self, sla: str = None):
        self.data["sla"] = sla
        return self.data["sla"]

    def _set_subject(self, subject: str = None):
        self.data["subject"] = subject
        return self.data["subject"]

    def _set_user_id(self, user_id: str = None):
        self.data["user_id"] = user_id
        return self.data["user_id"]

    def _set_data(
        self,
        token: str = None,
        api_key: str = None,
        body: str = None,
        email: str = None,
        first_name: str = None,
        helptopic: str = None,
        last_name: str = None,
        priority: str = None,
        sla: str = None,
        subject: str = None,
        code: str = None,
        dept: str = None,
        duedate: str = None,
        mobile: str = None,
        phone: str = None,
        user_id: str = None,
    ):
        self._set_token(token)
        self._set_api_key(api_key)
        self._set_body(body)
        self._set_email(email)
        self._set_first_name(first_name)
        self._set_helptopic(helptopic)
        self._set_last_name(last_name)
        self._set_priority(priority)
        self._set_sla(sla)
        self._set_subject(subject)
        self._set_code(code)
        self._set_dept(dept)
        self._set_deudate(duedate)
        self._set_mobile(mobile)
        self._set_phone(phone)
        self._set_user_id(user_id)
        return self.data

    def create_ticket(
        self,
        body: str,
        email: str,
        first_name: str,
        helptopic: str,
        last_name: str,
        priority: str,
        sla: str,
        subject: str,
        code: str = None,
        dept: str = None,
        duedate: str = None,
        mobile: str = None,
        phone: str = None,
        user_id: str = None,
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
        self._prepare_data()
        response = post(
            url=f"{self.url}/api/v1/helpdesk/create",
            headers=self.headers,
            json=self.data
        )
        return response.json()
