import random

def guess_number_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("Я загадал число от 1 до 100.")
    print(f"У вас есть {max_attempts} попыток, чтобы угадать его.")

    while attempts <= max_attempts:
        try:
            guess = int(input("Введите ваше предположение: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Слишком низко!")
            elif guess > number_to_guess:
                print("Слишком высоко!")
            else:
                print(f"Поздравляю! Вы угадали число {number_to_guess} за {attempts} попыток.")
                break
            if attempts == max_attempts:
                print(f"К сожалению, вы исчерпали все попытки. Загаданное число было {number_to_guess}.")
                break
        except ValueError:
            print("Пожалуйста, введите корректное целое число.")

if __name__ == "__main__":
    guess_number_game()