print('Мастям игральных карт присвоены порядковые номера '\
      '\n1 — пики'\
      '\n2 — трефы' \
      '\n3 — бубны',
      '\n4 — червы')
type_card = int(input('Вврдите маст карту : '))
card = int(input('Вводите значения карта (6...14) : '))

cards = {
    
    6 : 'щест',
    7 : 'семь',
    8 : 'восемь',
    9 : 'девять',
    10 : 'десять',
    11 : 'туз',
    12 : 'валет',
    13 : 'дама',
    14 : 'карол'
        
                  }
type_cards = {
    
    1 : 'пики',
    2 : 'трефы',
    3 : 'бубны',
    4 : 'червы'

                   }

if card in cards.keys() :
    mesage = cards[card]

    if type_card in type_cards.keys():
        mesage += f' {type_cards[type_card]}'
    
print(f'ВЫ вводили {mesage}')

