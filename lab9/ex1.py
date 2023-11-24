import requests

url = "https://jsonplaceholder.typicode.com/posts"

parameters = {"userId": 1}

response = requests.get(url=url, params=parameters)

if response.status_code == 200:
    posts = response.json()

    print(f"Numer of posts returned from the request: {len(posts)}")


else:
    print(f"Error: {response.status_code}")
