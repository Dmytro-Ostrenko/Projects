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
