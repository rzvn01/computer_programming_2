import requests


class HttpRequestHandler:
    @staticmethod
    def get(url):
        try:
            response = requests.get(url=url)

            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as exception:
            print(f"Get error occurred :{exception}")
            return None

    @staticmethod
    def post(url, data):
        try:
            response = requests.post(url=url, json=data)

            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as exception:
            print(f"Post error occurred :{exception}")
            return None


if __name__ == "__main__":
    http_handler = HttpRequestHandler();
    get_url = "https://jsonplaceholder.typicode.com/posts/1"
    print(f"Get result: {http_handler.get(get_url)}")

    post_url = "https://jsonplaceholder.typicode.com/posts"
    post_data = {"title": "foo", "body": "bar", "userId": 1}

    print(f"Post result: {http_handler.post(post_url, post_data)}")
