doorState = 'Дверь закрыта'   # Стартовый стейт двери
lockState = 'Замок закрыт'   # Стартовй стейт замка
command = ''  # Команда пользователя
print(doorState + '. ' + lockState)    # выводим стартовый стейт двери и замка
print('Доступные команды: Открыть/Закрыть, Отпереть/Запереть')    # указываем доступные команды

while not command == 'выйти':    # Выполняем цикл, пока юзер не введет "выйти"
    command = str(input('Введите команду: '))
    command = command.lower()    # делаем всю строку в нижнем регистре для сравнения условий

    if command == 'открыть':
        if doorState == 'Дверь открыта':
            print('Дверь уже открыта.')
        elif lockState == 'Замок закрыт':
            print('Сначала нужно открыть замок.')
        else:
            doorState = 'Дверь открыта'
            print(doorState + '. ' + lockState)

    elif command == 'закрыть':
        if doorState == 'Дверь закрыта':
            print('Дверь уже закрыта.')
        else:
            doorState = 'Дверь закрыта'
            print(doorState + '. ' + lockState)

    elif command == 'отпереть':
        if lockState == 'Замок открыт':
            print('Замок уже открыт.')
        else:
            lockState = 'Замок открыт'
            print(doorState + '. ' + lockState)

    elif command == 'запереть':
        if lockState == 'Замок закрыт':
            print('Замок уже закрыт.')
        elif doorState == 'Дверь открыта':
            print('Сначала нужно закрыть дверь.')
        else:
            lockState = 'Замок закрыт'
            print(doorState + '. ' + lockState)

    elif command == 'выйти':    #Вывод сообщения при завершении программы

        print('Программа закончена.')
    else:
        print('Ошибка ввода, введите команду еще раз!')