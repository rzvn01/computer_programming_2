import requests


def get_arena_count():
    url = "https://hamer.rcenter.cz/api/arena"

    try:
        response = requests.get(url)
        response.raise_for_status()

        arenas = response.json()
        arena_count = len(arenas)

        return arena_count

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    arena_count = get_arena_count()

    if arena_count is not None:
        print(f"There are {arena_count} arenas at the moment.")
