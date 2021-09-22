year = int(input('Вводите год : '))

animal =  (year - 1984) % 12 + 1
color =   (year - 1984) // 12  + 1 

while color > 5 :
    color -= 5

colors = {
          1 : 'зеленый', 
          2 : 'красный',
          3 : 'желтый',
          4 : 'белый', 
          5 : 'черный'
        }

animals = {
           1 : 'крысы',
           2 : 'коровы',
           3 : 'тигра',
           4 : 'зайца',
           5 : 'дракона',
           6 : 'змеи',
           7 : 'лошади',
           8 : 'овцы',
           9 : 'обезьяны',
          10 : 'курицы',
          11 : 'собаки',
          12 : 'свиньи'
                  }

result = ''


if color in colors.keys() :
    result += f'{colors[color]} '


if animal in animals.keys() :
    result += animals[animal]

print(result)
