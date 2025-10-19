def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = file.readlines()
            total = 0
            count = 0

            for line in salaries:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1

            average = total / count if count > 0 else 0
            return total, average

    except FileNotFoundError:
        print("Файл не знайдено, перевірте шлях!")
        return 0, 0
