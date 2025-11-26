import random

def draw_lotto_numbers(pool_size, draw_count):
    #Lottoziehung
    numbers = list(range(1, pool_size + 1))
    drawn_numbers = []

    for i in range(draw_count):
        index = random.randint(0, pool_size - 1 - i)
        drawn_number = numbers[index]
        drawn_numbers.append(drawn_number)
        #Gezogene Zahl ans Ende tauschen, damit sie nicht erneut gezogen wird (Logik)
        numbers[index], numbers[pool_size - 1 - i] = numbers[pool_size - 1 - i], numbers[index]

    return drawn_numbers


def update_statistics(statistics, drawn_numbers):
    #aktualisiert Dictionary
    for number in drawn_numbers:
        statistics[number] += 1


def run_lotto_simulation(pool_size, draw_count, simulation_count):
    # Dictionary aktualisieren: Anzahl, wie oft sie gezogen wurde
    statistics = {number: 0 for number in range(1, pool_size + 1)}

    for _ in range(simulation_count):
        drawn_numbers = draw_lotto_numbers(pool_size, draw_count)
        update_statistics(statistics, drawn_numbers)

    return statistics

def print_statistics(statistics):
    #Ausgabe
    print("Häufigkeit der gezogenen Zahlen:\n")
    for number in sorted(statistics.keys()):
        print(f"Zahl {number:2d}: {statistics[number]} mal")


def main():
    pool_size = 45           
    draw_count = 6           
    simulation_count = 1000

    statistics = run_lotto_simulation(pool_size, draw_count, simulation_count)
    print_statistics(statistics)

if __name__ == "__main__":
    main()
