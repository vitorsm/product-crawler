

class RequestException(Exception):
    def __init__(self, status: int, response: str):
        super(f"the request failed error {status}: {response}")
