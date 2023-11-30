import requests


def fetch_all_comments(post_id):
    url = "https://jsonplaceholder.typicode.com/comments"

    page = 1
    total_comments = []
    flag = 1

    while True:
        parameters = {"postId": post_id, "_page": page, "_limit": 10}

        response = requests.get(url=url, params=parameters)

        if response.status_code == 200:
            comments = response.json()

            if comments:
                total_comments.extend(comments)
            else:
                break
            page += 1
        else:
            print(f"Error : {response.status_code}")
            break
    return total_comments


print(f"Number of comments : {len(fetch_all_comments(1))}")
