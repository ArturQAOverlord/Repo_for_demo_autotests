import requests

url = "https://demoqa.ru/BookStore/v1/Books"

def Get_book_collection():
    payload = {}
    headers = {
    'accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200, f'Не удалось получить список скниг {response.status_code}'

    return response
