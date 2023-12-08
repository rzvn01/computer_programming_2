import requests


def create_arena(name, key):
    url = "https://hamer.rcenter.cz/api/arena"
    payload = {
        "name": name,
        "key": key
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()

        if response.status_code == 200:
            data = response.json()
            arena_id = data.get("_id")
            print(f"Arena created successfully! Arena ID: {arena_id}")

            return arena_id
        else:
            print(f"Failed to create arena. Status code: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def assign_bot_to_arena(bot_id, bot_key, arena_id, arena_key):
    url = f"https://hamer.rcenter.cz/api/arena"
    payload = {
        "_id": bot_id,
        "key": bot_key
    }
    headers = {
        "Content-Type": "application/json",
        "Arena-API-Key": arena_key
    }

    try:
        response = requests.put(f"{url}/{arena_id}", json=payload, headers=headers)
        response.raise_for_status()

        if response.status_code == 200:
            print("Bot assigned to the arena successfully!")
        else:
            print(f"Failed to assign bot to arena. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    arena_name = "BOT"
    arena_key = "54321"
    bot_name = "raszvan4"
    bot_key = "1234"
    bot_id = "6569b751272c8f113165f0ab"

    arena_id = create_arena(arena_name, arena_key)

    if arena_id is not None:
        # Assign Bot to Arena
        assign_bot_to_arena(bot_id=bot_id, bot_key=bot_key, arena_id=arena_id, arena_key=arena_key)
