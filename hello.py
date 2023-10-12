import arrow


def hello():
    """
    Function hello returns a "Hello, World!" string.

    >>> hello()
    'Hello, World!'
    """
    return "Hello, World!"


def unix_start():
    """
    Function unix_start retuns "1970-01-01T00:00:00+00:00" string.

    >>> unix_start()
    '1970-01-01T00:00:00+00:00'
    """
    return str(arrow.get(0))


if __name__ == "__main__":
    print(hello())
