class Team:
    def __init__(self, name: str, players: dict) -> None:
        self._name = name.lower()
        self._players = players
        self._points = 20

    def __str__(self):
        return f"Team's name: {self._name} | Players: {self._players}"