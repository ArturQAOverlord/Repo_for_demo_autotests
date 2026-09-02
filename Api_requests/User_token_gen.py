import requests
import json

url = "https://demoqa.ru/Account/v1/GenerateToken"

def User_token_gen(name, password):
    payload = json.dumps({
    "userName": name,
    "password": password
    })
    headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.status_code == 200, f'Токен не получен {response.status_code}'

    return response