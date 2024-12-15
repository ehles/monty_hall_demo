import random

def monty_hall_simulation(switch_strategy):
    # Случайным образом располагаем кофе за одной из дверей
    doors = ["чай", "чай", "кофе"]
    random.shuffle(doors)
    
    # Пользователь выбирает дверь случайным образом
    user_choice = random.randint(0, 2)
    
    # Открываем дверь с чаем
    if doors[user_choice] == "кофе":
        # Если пользователь угадал, открываем любую из оставшихся дверей с чаем
        remaining_doors = [i for i in range(3) if i != user_choice]
        opened_door = random.choice(remaining_doors)
    else:
        # Если пользователь не угадал, открываем дверь с чаем
        opened_door = [i for i in range(3) if i != user_choice and doors[i] == "чай"][0]
    
    # Если используется стратегия смены выбора
    if switch_strategy:
        # Изменяем выбор на оставшуюся дверь
        final_choice = [i for i in range(3) if i != user_choice and i != opened_door][0]
    else:
        # Оставляем первоначальный выбор
        final_choice = user_choice
    
    # Проверяем, выиграл ли пользователь
    return doors[final_choice] == "кофе"

def run_simulations(num_iterations, switch_strategy):
    wins = 0
    for _ in range(num_iterations):
        if monty_hall_simulation(switch_strategy):
            wins += 1
    return wins / num_iterations * 100

# Количество итераций для симуляции
num_iterations = 10000

# Симуляция с изменением выбора
switch_win_rate = run_simulations(num_iterations, switch_strategy=True)

# Симуляция без изменения выбора
stay_win_rate = run_simulations(num_iterations, switch_strategy=False)

# Вывод результатов
print(f"Симуляция с изменением выбора: {switch_win_rate:.2f}% успешных угадываний")
print(f"Симуляция без изменения выбора: {stay_win_rate:.2f}% успешных угадываний")

