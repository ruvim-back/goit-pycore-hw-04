def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # пропускаем пустые строки

                parts = line.split(',')
                if len(parts) != 3:
                    print(f"Невірний формат рядка: {line}")
                    continue

                cat_id, name, age = parts
                cats.append({"id": cat_id, "name": name, "age": age})

        return cats

    except FileNotFoundError:
        print("Файл не знайдено!")
        return []
