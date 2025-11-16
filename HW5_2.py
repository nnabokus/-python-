while True:
    a = float(input("Введіть перше число:"))
    b = float(input("Введіть друге число:"))
    action = input("Введіть дію (+, -, *, /):")

    if action == '+':
        print("Результат:", a + b)
    elif action == '-':
        print("Результат:", a - b)
    elif action == '*':
        print("Результат:", a * b)
    elif action == '/':
        if b != 0:
            print("Результат:", a / b)
        else:
            print("Неможливо поділити на 0!")
    else:
        print("Невідома дія")

    choice = input("Бажаєте продовжити? (y/yes): ").lower()

    if choice == "y" or choice == "yes":
      
    else:
        print("Калькулятор завершив роботу.")
        break
