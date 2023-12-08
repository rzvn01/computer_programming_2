import requests


def create_bot(name, key):
    url = "https://hamer.rcenter.cz/api/player"
    payload = {
        "name": name,
        "key": key
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()

        if response.status_code == 200:
            data = response.json()
            print(data)
            bot_id = data.get("_id")
            print(f"Bot created successfully! Bot ID: {bot_id}")

            save_bot_credentials(bot_id, key)
        else:
            print(f"Failed to create bot. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def save_bot_credentials(bot_id, key):
    print(f"Bot ID: {bot_id}, Key: {key}")

if __name__ == "__main__":
    bot_name = "razvan1234"
    bot_key = "1234"

    create_bot(bot_name, bot_key)
