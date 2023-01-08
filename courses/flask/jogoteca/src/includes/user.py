class User:
    def __init__(
        self,
        name: str,
        login: str,
        password: str
    ) -> None:
        self.name: str = name.title().strip()
        self.login: str = login.lower().strip()
        self.password: str = password
