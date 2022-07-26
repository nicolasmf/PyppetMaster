import random
import requests
from Puppet import Puppet
from browse import create_proton_account, create_instagram_account


def get_puppet():
    """
    Get new puppet from randomuser.me API
    """

    re = requests.get("https://randomuser.me/api/")

    results = re.json()["results"][0]

    puppet = Puppet(
        gender=results["gender"],
        first_name=results["name"]["first"],
        last_name=results["name"]["last"],
        street=str(results["location"]["street"]["number"])
        + " "
        + results["location"]["street"]["name"],
        city=results["location"]["city"],
        state=results["location"]["state"],
        country=results["location"]["country"],
        postcode=results["location"]["postcode"],
        username=results["email"].replace("@example.com", "")
        + str(random.randint(45658, 99999)),
        email=results["email"].replace("example.com", "proton.me"),
        picture=results["picture"]["large"],
    )

    return puppet


create_proton_account(get_puppet())

# create_instagram_account(get_puppet())
