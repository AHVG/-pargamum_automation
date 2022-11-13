

class ElementNotFoundException(Exception):

    def __init__(self, by, path) -> None:
        super().__init__(f"Element not found! By {by}, Path {path}")

class NoBooksException(Exception):

    def __init__(self) -> None:
        super().__init__(f"No books to be renewed!")
