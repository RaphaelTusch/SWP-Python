def filter_missing_values(temperatures):
    if not temperatures:
        return [], 0
    cleaned = []
    missing_count = 0

    for t in temperatures:
        if -60 <= t <= 60:
            cleaned.append(t)
        else:
            missing_count += 1
    return cleaned, missing_count


def calculate_average(temperatures):
    if not temperatures:
        return None

    return sum(temperatures) / len(temperatures)


def main():
    temp_values = [12, 15, -55, 18, 200, 22, -61, 9, 10, 14]
    cleaned_values, missing = filter_missing_values(temp_values)
    print(f"Bereinigte Liste: {cleaned_values}")
    print(f"Anzahl Fehlwerte: {missing}")
    avg = calculate_average(cleaned_values)
    if avg is None:
        print("Keine gültigen Werte")
    else:
        print(f"Durchschnittstemperatur: {avg:.2f} °C")

if __name__ == "__main__":
    main()
