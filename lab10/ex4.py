import requests
import math
import time


def find_nearest_food(bot_position, food_list):
    min_distance = float('inf')
    nearest_food = None

    for food in food_list:
        distance = math.sqrt((food['position']['x'] - bot_position[0]) ** 2 + (
                food['position']['y'] - bot_position[1]) ** 2)
        if distance < min_distance:
            min_distance = distance
            nearest_food = food

    return nearest_food


def calculate_move_vector(bot_position, target_position):
    delta_x = target_position['position']['x'] - bot_position[0]
    delta_y = target_position['position']['y'] - bot_position[1]

    magnitude = math.sqrt(delta_x ** 2 + delta_y ** 2)

    if magnitude > 1:
        delta_x /= magnitude
        delta_y /= magnitude

    move_vector = {"x": delta_x, "y": delta_y}

    return move_vector


def make_move(api_url, bot_key, move_vector):
    headers = {
        "Content-Type": "application/json",
        "Player-API-Key": bot_key
    }
    payload = {
        "move": {
            "x": move_vector['x'],
            "y": move_vector['y']
        }
    }

    try:
        response = requests.put(api_url, json=payload, headers=headers)
        response.raise_for_status()
        time.sleep(0.1)

    except requests.exceptions.RequestException as e:
        print(f"Error making move: {e}")


if __name__ == "__main__":
    # Replace these placeholders with your actual values
    arena_api_url = "https://hamer.rcenter.cz/api/arena/"
    arena_id = "656a4a47f1cb897d5bb8434b"
    bot_key = "1234"
    bot_id = "65699e8951ab621fc05762a2"
    url = "https://hamer.rcenter.cz/api/player/" + bot_id

    while True:
        try:

            bot_info_response = requests.get(url,
                                             headers={"Player-API-Key": bot_key})
            arena_info = requests.get(arena_api_url + arena_id)

            print(f"Bot Info Response: {bot_info_response.text}")
            print(f"Arena Info Response: {arena_info.text}")

            bot_info = bot_info_response.json()

            print(f"Bot Info: {bot_info}")

            if bot_info and arena_info:
                bot_position = (bot_info['position']['x'], bot_info['position']['y'])
                print("\n\n " + str(bot_position))
                food_list = arena_info.json().get('foods')

                print(f"Bot Position: {bot_position}")

                if bot_position and food_list:
                    nearest_food = find_nearest_food(bot_position, food_list)

                    print(f"Nearest Food: {nearest_food}")

                    if nearest_food:
                        move_vector = calculate_move_vector(bot_position, nearest_food)
                        print(f"Move Vector: {move_vector}")
                        make_move(url, bot_key, move_vector)

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

        time.sleep(1)
