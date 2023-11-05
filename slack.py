from datetime import date, timedelta, datetime

def get_birthdays_per_week(users):
    if not users:
        return {}
    current_date = date.today()
    weekdays = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday' } 
  
    birthdays_per_week = {day: [] for day in weekdays.values()} 
    for user in users:
        name = user['name']
        birthday = user['birthday'] 
        next_birthday = birthday.replace(year=current_date.year)
        if next_birthday < current_date:
            next_birthday = next_birthday.replace(year=current_date.year + 1)
        # Перевіряємо, чи дата народження потрапляє в наступний тиждень
        if current_date <= next_birthday <= current_date + timedelta(days=7):
            day_of_week = next_birthday.weekday()
            day_name = weekdays[day_of_week]  # Отримуємо назву дня тижня
            # Перевірка, чи день народження падає на вихідний
            if day_name in ['Saturday', 'Sunday']:
                day_name = 'Monday'  # Переносимо на понеділок
            birthdays_per_week[day_name].append(name)
    birthdays_per_week = {day: names for day, names in birthdays_per_week.items() if names}
    print(birthdays_per_week)
    return birthdays_per_week


if __name__ == "__main__":
    users = [
        {'name': 'Masha', 'birthday': date(2023, 11, 9)},
        {'name': 'Olya', 'birthday': date(2023, 11, 3)},
        {'name': 'Kolya', 'birthday': date(2023, 11, 4)},
        {'name': 'Sophia', 'birthday': date(2023, 11, 5)},
        {'name': 'Solomia', 'birthday': date(2023, 11, 6)},
        {'name': 'Sasha', 'birthday': date(2023, 11, 7)},
        {'name': 'Pasha', 'birthday': date(2023, 11, 8)},
        {'name': 'Oksana', 'birthday': date(2023, 11, 10)}
    ]
    result = get_birthdays_per_week(users)
    # Виведення результатів
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")