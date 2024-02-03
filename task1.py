import pulp


def main():
    # Ініціалізація моделі
    model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

    # Визначення змінних
    limo = pulp.LpVariable('Лімонад', lowBound=0, cat=pulp.LpContinuous)
    fj = pulp.LpVariable('Фруктовий сік', lowBound=0, cat=pulp.LpContinuous)
    water1 = pulp.LpVariable('Вода1', lowBound=0, cat=pulp.LpContinuous)
    water2 = pulp.LpVariable('Вода2', lowBound=0, cat=pulp.LpContinuous)
    sugar = pulp.LpVariable('Цукор', lowBound=0, upBound=50, cat=pulp.LpContinuous)
    limo_juse = pulp.LpVariable('Лимонний сік', lowBound=0, upBound=30, cat=pulp.LpContinuous)
    fruit_pure = pulp.LpVariable('Фруктове пюре', lowBound=0, upBound=40, cat=pulp.LpContinuous)

    # Функція цілі (Максимізація прибутку)
    model += fj + limo, "Profit"

    # Додавання обмежень
    model += 0.5 * water1 - limo >= 0
    model += sugar - limo >= 0
    model += limo_juse - limo >= 0
    model += water2 - fj >= 0
    model += 0.5 * fruit_pure - fj >= 0
    model += water1 + water2 <= 100


    # Розв'язання моделі
    model.solve()

    print(pulp.LpStatus[model.status])

    # Вивід результатів
    print("Виробляти Лимонаду:", limo.varValue)
    print("Виробляти Фруктового соку:", fj.varValue)

if __name__ == '__main__':
    main()