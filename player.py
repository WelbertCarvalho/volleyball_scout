class Player:
    def __init__(self, name, position, team) -> None:
        self._name = name.lower()
        self._position = position.lower()
        self._team = team.lower()

    def __str__(self):
        return f'Player: {self._name} | Position: {self._position} | Team: {self._team}'