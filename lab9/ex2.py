import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "My New Post",
    "body": "This is the body of my new post.",
    "userId": 1
}

request = requests.post(url=url, json=payload)

if request.status_code == 201:
    post = request.json()

    print(f"Status code : {request.status_code}")
    print(f"ID of the created post: {post['id']}")

else :
    print(f"Error : {request.status_code}")
