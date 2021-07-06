

class RequestException(Exception):
    def __init__(self, status: int, response: str):
        super().__init__(f"the request failed error {status}: {response}")
