import requests


def fetch_all_comments(post_id):
    url = "https://jsonplaceholder.typicode.com/comments"

    total_comments = []

    parameters = {"postId": post_id}

    response = requests.get(url=url, params=parameters)

    if response.status_code == 200:
        total_comments = response.json()

    else:
        print(f"Error : {response.status_code}")

    return total_comments


print(len(fetch_all_comments(1)))
