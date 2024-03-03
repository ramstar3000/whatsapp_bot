import requests

def read_params(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    api_key = lines[0].strip()
    id_instance = lines[1].strip()
    return api_key, id_instance

def send_message(file_name, message, phone_number="447401737792"):


    api_key, id_instance = read_params(file_name)

    response = requests.post(
        f"https://api.greenapi.com/waInstance{id_instance}/sendMessage/{api_key}",
        json={
            "chatId": f"{phone_number}@c.us",
            "message": message
        },
        timeout=10)
    print(response.json())

def send_group(file_name, message, group_id="120363168727472971"):

    api_key, id_instance = read_params(file_name)

    response = requests.post(
        f"https://api.greenapi.com/waInstance{id_instance}/sendMessage/{api_key}",
        json={
            "chatId": f"{group_id}@g.us",
            "message": message
        },
        timeout=10)
    print(response.json())

