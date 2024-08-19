execute = True

team = {}

map_positions = {
    '1': 'Setter',
    '2': '1º Outside Hitter',
    '3': '2º Outside Hitter',
    '4': '1º Middle Blocker',
    '5': '2º Middle Blocker',
    '6': 'Oposite Hitter',
    '7': 'Libero'
}

while execute:
    player = input('Type the name of the player: ')
    print(f'---------- Choose a position to {player} ----------')
    print('1 - Settter')
    print('2 - 1º Outside Hitter')
    print('3 - 2º Outside Hitter')
    print('4 - 1º Midle Blocker')
    print('5 - 2º Midle Blocker')
    print('6 - Oposite Hitter')
    print('7 - Libero')

    posicao = input('Type the corresponding number: ')

    team[player] = map_positions[posicao]

    continue_program = input('Continue?(y/n): ')
    if continue_program == 'n':
        execute = False
        print('Ending...')

    
print(team)

