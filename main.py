import math

def simple(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i <= math.isqrt(n):  # math.isqrt()
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_twin_primes(start, end):
    twin_primes = []
    for i in range(start, end - 1):
        if simple(i) and simple(i + 2):
            twin_primes.append((i, i + 2))
    return twin_primes

def write_results_to_file(filename, twin_primes, delimiter=",", format="row"):
    if format != "row" and format != "column":
        print("Ошибка: Неверный формат вывода.  Используйте 'row' или 'column'.")
        return  # Прерываем выполнение, не создавая файл
    try:
        with open(filename, "w") as f: #Файл откроется только если формат корректный
            for pair in twin_primes:
                if format == "row":
                    f.write(f"{pair[0]}{delimiter}{pair[1]}\n")
                elif format == "column":
                    f.write(f"{pair[0]}\n{pair[1]}\n")
        print(f"Результаты записаны в файл: {filename}")
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")


try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    filename = input("Введите имя файла для сохранения результатов (или оставьте пустым для вывода в консоль): ")
    delimiter = input("Введите разделитель между числами (по умолчанию ','): ") or "," #Разделитель по умолчанию - запятая
    format = input("Введите формат вывода ('row' или 'column', по умолчанию 'row'): ") or "row" #Формат по умолчанию - строка

except ValueError:
    print("Ошибка: Введите целые числа.")
    exit()

start = min(a, b)
end = max(a, b)

twin_primes = find_twin_primes(start, end)

if twin_primes:
    if filename:
        write_results_to_file(filename, twin_primes, delimiter, format)
    else:
        for pair in twin_primes:
            print(pair[0], pair[1])
else:
    print("Ничего")