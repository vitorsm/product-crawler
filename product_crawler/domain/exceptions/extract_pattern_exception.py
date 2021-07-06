

class ExtractPatternException(Exception):
    def __init__(self, message: str):
        super(f"Error to extract content from HTML, pattern error: {message}")
