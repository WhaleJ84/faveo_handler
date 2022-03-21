# Faveo Handler

A Python library to interact with the Faveo API

## Installation

This repository is designed to be used as a Pip module. You can pull it by running the following:

```shell script
# Pip
python3 -m pip install git+https://github.com/WhaleJ84/faveo_handler.git

# Pipenv
python3 -m pipenv install -e git+https://github.com/WhaleJ84/faveo_handler.git#egg=faveo_handler
```

## Usage

The following is an example script that utilises the authenticate, create, read, and delete endpoints.

```python
from os import getenv
from pprint import pprint

from faveo_handler import FaveoHandler

api = FaveoHandler("https://faveo.example.com")
api.authenticate(getenv("FAVEO_USERNAME"), getenv("FAVEO_PASSWORD"))
ticket_id = api.create_ticket(
    body="test body of at least ten characters",
    email="admin@example.com",
    first_name="Mr",
    helptopic="1",
    last_name="Administrator",
    priority="1",
    sla="1",
    subject="test subject"
)["response"]["ticket_id"]
pprint(api.get_tickets())
api.delete_ticket(ticket_id)
```
