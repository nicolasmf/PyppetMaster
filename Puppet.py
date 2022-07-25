from dataclasses import dataclass


@dataclass()
class Puppet:
    gender: str
    first_name: str
    last_name: str
    street: str
    city: str
    state: str
    country: str
    postcode: str
    username: str
    email: str
    picture: str
