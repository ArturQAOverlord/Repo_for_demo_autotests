import pytest
from faker import Faker

from Api_requests.User_creation import User_creation
from Api_requests.User_deletion import User_deletion
from Api_requests.User_exist_check import User_exist_check
from Api_requests.User_token_gen import User_token_gen
from Api_requests.Get_book_collection import Get_book_collection

@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": False,
        "slow_mo": 300,
    }


@pytest.fixture
def user():
    fake = Faker()
    username = fake.user_name()
    password = fake.password()

    response = User_creation(username, password)
    user_id = response.json()["userId"]

    token = User_token_gen(username, password).json()['token']
    User_exist_check(user_id, token)

    book_list = Get_book_collection().json()

    yield {
        "username": username,
        "password": password,
        "user_id": user_id,
        "book_list": book_list
    }

    User_deletion(user_id, token)