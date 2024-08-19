from game import Game
from team import Team
from player import Player

bruninho = Player(name = 'Bruninho', position = 'Levantador', team = 'Brasil')
thales = Player(name = 'Thales', position = 'Líbero', team = 'Brasil')
leal = Player(name = 'Leal', position = 'Ponteiro', team = 'Brasil')
darlan = Player(name = 'Darlan', position = 'Oposto', team = 'Brasil')
lucarelli = Player(name = 'Lucarelli', position = 'Ponteiro', team = 'Brasil')
lucao = Player(name = 'Lucão', position = 'Central', team = 'Brasil')
flavio = Player(name = 'Flávio', position = 'Central', team = 'Brasil')

brasil = Team(
    name =  'Brasil',
    players = {
        bruninho._name: bruninho,
        thales._name: thales,
        leal._name: leal,
        darlan._name: darlan,
        lucarelli._name: lucarelli,
        lucao._name: lucao,
        flavio._name: flavio
    }
)

anderson = Player(name = 'Matt Anderson', position = 'oposto', team = 'EUA')
chistenson = Player(name = 'Micah Chistenson', position = 'Levantador', team = 'EUA')
holt = Player(name = 'Max Holt', position = 'Central', team = 'EUA')
shoji = Player(name = 'Erik Shoji', position = 'Líbero', team = 'EUA')
defalco = Player(name = 'TJ DeFalco', position = 'Ponteiro', team = 'EUA')
russell = Player(name = 'Aaron Russell', position = 'Ponteiro', team = 'EUA')
averill = Player(name = 'Taylor Averill', position = 'Central', team = 'EUA')

eua = Team(
    name = 'EUA',
    players = {
        anderson._name: anderson,
        chistenson._name: anderson,
        holt._name: holt,
        shoji._name: shoji,
        defalco._name: defalco,
        russell._name: russell,
        averill._name: averill
    }
)

brasil_eua = Game(
    team_1 = brasil,
    team_2 = eua
)

print(brasil_eua)


brasil_eua.point(team = 'Brasil')
brasil_eua.point(team = 'brasil')
brasil_eua.point(team = 'brasil')
brasil_eua.point(team = 'brasil')


brasil_eua.point(team = 'eua')
brasil_eua.point(team = 'EUA')
brasil_eua.point(team = 'eua')
brasil_eua.point(team = 'eua')


placar_set = brasil_eua.set_score()
print(placar_set)

brasil_eua.point(team = 'brasil')

placar_set = brasil_eua.set_score()
print(placar_set)

brasil_eua.point(team = 'brasil')

placar_set = brasil_eua.set_score()
print(placar_set)


placar_jogo = brasil_eua.game_score()
print(placar_jogo)

print(brasil_eua._sets)

