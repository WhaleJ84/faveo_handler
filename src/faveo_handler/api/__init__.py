class FaveoApi:
    def __init__(self, url: str, api_key: str = None):
        """
        :param url: Base URL to the Faveo instance. e.g. `https://faveo.example.com'
        :param api_key: An alphanumeric code that can be used to authenticate your API calls.
        To make it required login to Admin panel and go to API setting and make it mandatory
        """
        self.url = url.strip("/")
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        self._data = {
            # Base
            "token": None,
            "api_key": api_key,
            # Helpdesk/Create
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
            # Helpdesk/Update&Delete
            "ticket_id": None,
            # Helpdesk/Update
            "ip": None,
            "reply_content": None,
        }
        self.data = self._data

    def _set_url(self, url: str = None):
        self.url = url.strip("/")
        return self.url

    def _set_headers(self, headers: dict = None):
        self.headers = headers
        return self.headers

    def _set_token(self, token: str = None):
        # Token does not necessarily want to be wiped every time the data is cleared
        # This will keep the original value unless stated otherwise
        if not token:
            try:
                token = self.data["token"]
            except KeyError:
                pass
        self.data["token"] = token
        return self.data["token"]

    def _set_api_key(self, api_key: str = None):
        # API key does not want to be wiped every time the data is cleared
        # This will keep the original value unless stated otherwise
        if not api_key:
            try:
                api_key = self.data["api_key"]
            except KeyError:
                pass
        self.data["api_key"] = api_key
        return self.data["api_key"]

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

    def _set_ticket_id(self, ticket_id: str = None):
        self.data["ticket_id"] = ticket_id
        return self.data["ticket_id"]

    def _set_ip(self, ip: str = None):
        self.data["ip"] = ip
        return self.data["ip"]

    def _set_reply_content(self, reply_content: str = None):
        self.data["reply_content"] = reply_content
        return self.data["reply_content"]

    def _remove_none_values_from_data(self):
        for key, value in list(self.data.items()):
            if value is None:
                del self.data[key]
        return self.data

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
        ticket_id: str = None,
        ip: str = None,
        reply_content: str = None,
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
        self._set_ticket_id(ticket_id)
        self._set_ip(ip)
        self._set_reply_content(reply_content)
        self._remove_none_values_from_data()
        return self.data
