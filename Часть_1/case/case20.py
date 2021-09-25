print('Вводите два целых числа: D (день) и M (месяц)')

day = int(input('D (день) : '))
month = int(input('M (месяц) : '))

days =  list(range(1,32))
months = list(range(1,13))

zadiyak = {
    
    "Водолей" : {
        1  : list(range(20,32)),
        2  : list(range(1,19))    },
    
    "Рыбы"    : {
        2  : list(range(19,28)),
        3  : list(range(1,21))    },
    
    "Овен"    : {
        3  : list(range(21,32)),
        4  : list(range(1,20))    },
    
    "Телец"    : {
        4  : list(range(21,31)),
        5  : list(range(1,20))    },
    
    "Близнецы"    : {
        5  : list(range(21,32)),
        6  : list(range(1,22))    },

    "Рак"    : {
        6  : list(range(22,31)),
        7  : list(range(1,23))    },
    
    "Лев"    : {
        7  : list(range(23,32)),
        8  : list(range(1,23))    },
    
    "Дева"    : {
        8  : list(range(23,32)),
        9  : list(range(1,23))    },
    
    "Весы"    : {
        9  : list(range(23,31)),
        10  : list(range(1,23))    },
    
    "Скорпион"    : {
        10  : list(range(23,32)),
        11  : list(range(1,23))    },
    
    "Стрелец"    : {
        11  : list(range(23,31)),
        12  : list(range(1,22))    },

    "Козерог"    : {
        12  : list(range(22,32)),
        12  : list(range(1,20))    }
    
                                           }


        