from datetime import date, timedelta, datetime

def get_birthdays_per_week(users):
    #Реалізація ДЗ
    #1.Випадок пустого списку
    if not users:
        return {}
    current_date = date.today() #Створення поточної дати
    weekdays = {
        0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
        4: 'Friday', 5: 'Monday', 6: 'Monday'
    }
    
    #створення словника із іменами днів тижня(keys) і порожніми списками (values)  
    birthdays_per_week = {}
    for day in weekdays.values():
        birthdays_per_week[day] = []
  
    for user in users:
        name = user['name']
        birthday = user['birthday'] 
        #Замінюємо у ДР користувачів рік ДР на поточний 
        next_birthday  = user.get('birthday').replace(year=current_date.year)
        #Перевірка: якщо ДР вже був, то рік ДР +1(на наступний рік)
        if next_birthday < current_date:
            next_birthday = next_birthday.replace(year=current_date.year + 1)
        # Перевірка ДР, що буде на наступному тиждні
        if current_date <= next_birthday <= current_date + timedelta(days=7):
            day_of_week = next_birthday.weekday() #переноимо ДР на наступний диждень
            day_name = weekdays[day_of_week]  # беремо назву дня ДР
            # Якщо ДР випаде на вихідні, вітаємо у понеділок П
            if day_name in ['Saturday', 'Sunday']:
                day_name = 'Monday'  
            birthdays_per_week[day_name].append(name)# додаємо до словника за ключем (день тиждня, значення)
    #Видаляємо пусті дні списку, тобто без наявних ДР
    for day, names in list(birthdays_per_week.items()):
        if not names:
            del birthdays_per_week[day]
      
    return birthdays_per_week
 
if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
