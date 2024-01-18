# Инициализация базы вакансий
vacancies = [
    {'Должность': 'Менеджер по продажам', 'Необходимый стаж(лет работы)': 2, 'Пол': 'Любой', 'Образование': 'высшее', 'Минимальный возраст(годы)': 21, 'Максимальный возраст(годы)': 35, 'Знание иностранных языков': 'английский', 'Минимальный оклад(рублей)': 30000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 3},
    {'Должность': 'HR-менеджер', 'Необходимый стаж(лет работы)': 3, 'Пол': 'Любой', 'Образование': 'высшее', 'Минимальный возраст(годы)': 23, 'Максимальный возраст(годы)': 40, 'Знание иностранных языков': 'французский', 'Минимальный оклад(рублей)': 40000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 6},
    {'Должность': 'Программист', 'Необходимый стаж(лет работы)': 5, 'Пол': 'Мужской', 'Образование': 'высшее', 'Минимальный возраст(годы)': 25, 'Максимальный возраст(годы)': 45, 'Знание иностранных языков': 'немецкий', 'Минимальный оклад(рублей)': 50000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 3},
    {'Должность': 'Бухгалтер','Необходимый стаж(лет работы)': 4, 'Пол': 'Любой', 'Образование': 'Высшее экономическое', 'Минимальный возраст(годы)': '30 лет',  'Максимальный возраст(годы)': 60, 'Знание иностранных языков': 'Английский (средний уровень)', 'Минимальный оклад(рублей)': 90000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 6},
    {'Должность': 'Медицинская сестра', 'Необходимый стаж(лет работы)': 3, 'Пол': 'Женский','Образование': 'Среднее медицинское','Минимальный возраст(годы)': 25 ,'Максимальный возраст(годы)': 55,'Знание иностранных языков': 'Не требуется','Минимальный оклад(рублей)': 60000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 3},
    {'Должность': 'Адвокат', 'Необходимый стаж(лет работы)': 5, 'Пол': 'Любой', 'Образование': 'Высшее юридическое', 'Минимальный возраст(годы)': '30 лет', 'Максимальный возраст(годы)': 65, 'Знание иностранных языков': 'Английский (продвинутый уровень)', 'Минимальный оклад(рублей)': 100000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 6},
    {'Должность': 'Учитель начальных классов','Необходимый стаж(лет работы)': 2, 'Пол': 'Женский', 'Образование': 'Высшее педагогическое', 'Минимальный возраст(годы)': 25, 'Максимальный возраст(годы)': 55, 'Знание иностранных языков': 'Не требуется', 'Минимальный оклад(рублей)': 55000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 3},
    {'Должность': 'Механик','Необходимый стаж(лет работы)': 3, 'Пол': 'Любой', 'Образование': 'Среднее профессиональное', 'Минимальный возраст(годы)': 24, 'Максимальный возраст(годы)': 58, 'Знание иностранных языков': 'Не требуется', 'Минимальный оклад(рублей)': 60000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 4},
    {'Должность': 'Швея', 'Необходимый стаж(лет работы)': 2, 'Пол': 'Женский', 'Образование': 'Среднее профессиональное', 'Минимальный возраст(годы)': 23, 'Максимальный возраст(годы)': 50, 'Знание иностранных языков': 'Не требуется', 'Минимальный оклад(рублей)': 48000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 3},
    {'Должность': 'Архитектор', 'Необходимый стаж(лет работы)': 5, 'Пол': 'Любой', 'Образование': 'Высшее архитектурное', 'Минимальный возраст(годы)': 28, 'Максимальный возраст(годы)': 60, 'Знание иностранных языков': 'Английский (средний уровень)', 'Минимальный оклад(рублей)': 90000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 5},
    {'Должность': 'Менеджер по продажам', 'Необходимый стаж(лет работы)': 3, 'Пол': 'Любой', 'Образование': 'Высшее экономическое или коммерческое', 'Минимальный возраст(годы)': 25, 'Максимальный возраст(годы)': 50, 'Знание иностранных языков': 'Английский (разговорный уровень)', 'Минимальный оклад(рублей)': 70000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 3},
    {'Должность': 'Финансовый аналитик', 'Необходимый стаж(лет работы)': 2, 'Пол': 'Любой', 'Образование': 'Высшее экономическое', 'Минимальный возраст(годы)': 24, 'Максимальный возраст(годы)': 55, 'Знание иностранных языков': 'Английский (продвинутый уровень)', 'Минимальный оклад(рублей)': 80000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 4},
    {'Должность': 'Инженер-программист', 'Необходимый стаж(лет работы)': 2, 'Пол': 'Любой', 'Образование': 'Высшее техническое', 'Минимальный возраст(годы)': 23, 'Максимальный возраст(годы)': 50, 'Знание иностранных языков': 'Английский (продвинутый уровень)', 'Минимальный оклад(рублей)': 75000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 4},
    {'Должность': 'Медсестра', 'Необходимый стаж(лет работы)': 2, 'Пол': 'Женский', 'Образование': 'Среднее медицинское', 'Минимальный возраст(годы)': 22, 'Максимальный возраст(годы)': 55, 'Знание иностранных языков': 'Не требуется', 'Минимальный оклад(рублей)': 40000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 3},
    {'Должность': 'Разработчик веб-приложений', 'Необходимый стаж(лет работы)': 3, 'Пол': 'Любой', 'Образование': 'Высшее техническое или информационные технологии', 'Минимальный возраст(годы)': 24, 'Максимальный возраст(годы)': 50, 'Знание иностранных языков': 'Английский (продвинутый уровень)', 'Минимальный оклад(рублей)': 85000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 3},
    {'Должность': 'Специалист по маркетингу', 'Необходимый стаж(лет работы)': 2, 'Пол': 'не имеет значения', 'Образование': 'высшее образование в области маркетинга или экономики', 'Минимальный возраст(годы)': 25, 'Максимальный возраст(годы)': 'не ограничено', 'Знание иностранных языков': 'английский - свободное владение', 'Минимальный оклад(рублей)': 50000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 3},
    {'Должность': 'Программист', 'Необходимый стаж(лет работы)': 3, 'Пол': 'не имеет значения', 'Образование': 'высшее образование в области информационных технологий или компьютерных наук', 'Минимальный возраст(годы)': 22, 'Максимальный возраст(годы)': 'не ограничено', 'Знание иностранных языков': 'английский - технический перевод', 'Минимальный оклад(рублей)': 70000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 2},
    {'Должность': 'Медицинская сестра', 'Необходимый стаж(лет работы)': 1, 'Пол': 'женский', 'Образование': 'медицинское', 'Минимальный возраст(годы)': 21, 'Максимальный возраст(годы)': 55, 'Знание иностранных языков': 'не требуется', 'Минимальный оклад(рублей)': 40000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 3},
    {'Должность': 'Адвокат', 'Необходимый стаж(лет работы)': 5, 'Пол': 'не имеет значения', 'Образование': 'высшее юридическое образование' ,'Минимальный возраст(годы)': 30, 'Максимальный возраст(годы)': 60, 'Знание иностранных языков': 'английский - свободное владение', 'Минимальный оклад(рублей)': 80000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 6},
    {'Должность': 'Бухгалтер', 'Необходимый стаж(лет работы)': 3, 'Пол': 'не имеет значения', 'Образование': 'высшее образование в области бухгалтерского учета или экономики', 'Минимальный возраст(годы)': 23, 'Максимальный возраст(годы)': 55, 'Знание иностранных языков': 'не требуется', 'Минимальный оклад(рублей)': 55000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 3},
    {'Должность': 'Инженер-конструктор', 'Необходимый стаж(лет работы)': 2, 'Пол': 'не имеет значения', 'Образование': 'высшее техническое образование', 'Минимальный возраст(годы)': 24, 'Максимальный возраст(годы)': 65, 'Знание иностранных языков': 'английский - технический перевод', 'Минимальный оклад(рублей)': 60000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 3},
    {'Должность': 'Менеджер по продажам', 'Необходимый стаж(лет работы)': 2, 'Пол': 'не имеет значения', 'Образование': 'высшее образование в области маркетинга или экономики', 'Минимальный возраст(годы)': 25, 'Максимальный возраст(годы)': 45, 'Знание иностранных языков': 'английский - свободное владение', 'Минимальный оклад(рублей)': 50000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 3},
    {'Должность': 'Учитель начальных классов', 'Необходимый стаж(лет работы)': 3, 'Пол': 'не имеет значения', 'Образование': 'педагогическое образование', 'Минимальный возраст(годы)': 30, 'Максимальный возраст(годы)': 65, 'Знание иностранных языков': 'не требуется', 'Минимальный оклад(рублей)': 45000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 3},
    {'Должность': 'Инфограф', 'Необходимый стаж(лет работы)': 2, 'Пол': 'не имеет значения', 'Образование': 'высшее образование в области дизайна или искусств', 'Минимальный возраст(годы)': 23, 'Максимальный возраст(годы)': 55, 'Знание иностранных языков': 'английский - свободное владение', 'Минимальный оклад(рублей)': 55000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 2},
    {'Должность': 'Веб-разработчик', 'Необходимый стаж(лет работы)': 2, 'Пол': 'не имеет значения', 'Образование': 'высшее образование в области информационных технологий или компьютерных наук', 'Минимальный возраст(годы)': 24, 'Максимальный возраст(годы)': 50, 'Знание иностранных языков': 'английский - технический перевод', 'Минимальный оклад(рублей)': 60000, 'Наличие соцпакета': True, 'Испытательный срок(месяцев)': 3}
]

#Функция сортировки Хоара
def hoare_sort(arr, left, right, key):
    if left >= right:
        return
    pivot = arr[(left + right) // 2][key]
    i, j = left, right
    while i <= j:
        while arr[i][key] < pivot:
            i += 1
        while arr[j][key] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i, j = i + 1, j - 1
    hoare_sort(arr, left, j, key)
    hoare_sort(arr, i, right, key)


# Функция для добавления вакансии в базу
def add_vacancy():
    print(('Должность: Менеджер по продажам', 'Необходимый стаж(лет работы): 2', 'Пол: Любой', 'Образование: высшее', 'Минимальный возраст(годы): 21', 'Максимальный возраст(годы): 35', 'Знание иностранных языков: английский', 'Минимальный оклад(рублей): 30000', 'Наличие соцпакета: Да', 'Испытательный срок(месяцев): 3'))
    new_vacancy = {input("Введите данные о новой вакинсии согласно примеру выше: ")}
    # Ввод данных о вакансии с клавиатуры

    vacancies.append(new_vacancy)
    print("Вакансия успешно добавлена.")

# Функция для удаления вакансии из базы
def remove_vacancy():
    # Вывод списка вакансий с номерами для выбора пользователем
    for i, vacancy in enumerate(vacancies):
        print(f"{i+1}. {vacancy['Должность']}")

    index = int(input("Введите номер вакансии для удаления: "))
    vacancies.pop(index-1)
    print("Вакансия успешно удалена.")

# Функция для изменения данных о вакансии
def edit_vacancy():
    # Аналогично функции remove_vacancy, пользователь выбирает вакансию для изменения
    # Затем вводятся новые данные о вакансии

    for i, vacancy in enumerate(vacancies):
        print(f"{i+1}. {vacancy['Должность']}")

    index = int(input("Введите номер вакансии для изменения: "))
    print("Для изменения вам нужно будет полностью переписать данные вместе с изменениями.")
    vacancies[index - 1] = input("Введите изменения: ")
    print("Вакансия успешно изменена.")

# Функция для вывода всех вакансий
def print_all_vacancies():
    hoare_sort(vacancies, 0, len(vacancies) - 1, 'Образование')
    hoare_sort(vacancies, 0, len(vacancies) - 1, 'Должность')

    for vacancy in vacancies:
        print(vacancy)

# Функция для вывода списка вакансий с заданным испытательным сроком, стажем работы и максимальным возрастом,  сортировкой
def print_vacancies_by_trial_period(trial_period):
    filtered_vacancies = [vacancy for vacancy in vacancies if vacancy['Испытательный срок(месяцев)'] >= trial_period]

    hoare_sort(filtered_vacancies, 0, len(filtered_vacancies) - 1, 'Испытательный срок(месяцев)')
    hoare_sort(filtered_vacancies, 0, len(filtered_vacancies) - 1, 'Необходимый стаж(лет работы)')
    hoare_sort(filtered_vacancies, 0, len(filtered_vacancies) - 1, 'Максимальный возраст(годы)')

    for vacancy in filtered_vacancies:
        print(vacancy)



# Функция для вывода списка вакансий с окладом в заданном диапазоне
def print_vacancies_by_salary_range(min_salary, max_salary):

    # Фильтрация списка вакансий по заданному диапазону оклада
    filtered_vacancies = [vacancy for vacancy in vacancies if min_salary <= vacancy['Минимальный оклад(рублей)'] <= max_salary]

    # Сортировка отфильтрованного списка вакансий
    hoare_sort(filtered_vacancies, 0, len(filtered_vacancies) - 1, 'Наличие соцпакета')
    hoare_sort(filtered_vacancies, 0, len(filtered_vacancies) - 1, 'Испытательный срок(месяцев)')

    # Вывод отсортированного списка вакансий
    for vacancy in filtered_vacancies:
        print(vacancy)


# Основная функция программы
def main():
    while True:
        print("\nМеню:")
        print("1. Добавить вакансию")
        print("2. Удалить вакансию")
        print("3. Изменить вакансию")
        print("4. Вывести все вакансии")
        print("5. Вывести вакансии с определенным испытательным сроком")
        print("6. Вывести вакансии с окладом в заданном диапазоне")
        print("7. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_vacancy()
        elif choice == "2":
            remove_vacancy()
        elif choice == "3":
            edit_vacancy()
        elif choice == "4":
            print_all_vacancies()
        elif choice == "5":
            trial_period = int(input("Введите испытательный срок (например, '3 месяца'): "))
            print_vacancies_by_trial_period(trial_period)
        elif choice == "6":
            min_salary = int(input("Введите минимальный оклад: "))
            max_salary = int(input("Введите максимальный оклад: "))
            print_vacancies_by_salary_range(min_salary, max_salary)
        elif choice == "7":
            break
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
