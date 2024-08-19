from team import Team

class Game:
    def __init__(self, team_1: Team, team_2: Team) -> None:
        self._team_1 = team_1
        self._team_2 = team_2
        self._sets = {'team_1' : 0, 'team_2' : 0}

    def __str__(self) -> str:
        return f'Game between {self._team_1._name} X {self._team_2._name}.'
    
    def point(self, team: str) -> None:
        team = team.lower()
        if self._team_1._name == team:
            self._team_1._points += 1
        elif self._team_2._name == team:
            self._team_2._points += 1
        else:
            "Incorrect name for the team. Please, type a correct team's name"
        
        return None

    def set_won(self, set_winner: str) -> None:
        if set_winner == self._team_1._name:
            self._sets['team_1'] += 1
            return self._team_1._name
        elif set_winner == self._team_2._name:
            self._sets['team_2'] += 1
            return self._team_2._name
    
    def _check_set(self) -> str:
        if self._team_1._points >= 25 and (self._team_1._points - self._team_2._points) >= 2:
            return self.set_won(set_winner = self._team_1._name)
        elif self._team_2._points >= 25  and (self._team_2._points - self._team_1._points) >= 2:
            return self.set_won(set_winner = self._team_2._name)
        else:
            return 'Set in progress'

    def set_score(self) -> str:
        set_winner = self._check_set()
        return f'{self._team_1._name} {self._team_1._points} X {self._team_2._points} {self._team_2._name} - {set_winner}'


    def game_score(self) -> str:
        return f"{self._team_1._name} {self._sets['team_1']} X {self._sets['team_2']} {self._team_2._name}"
