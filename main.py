from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.validate(value)
        self.__value = value

    def validate(self, value):
        pass

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Введіть, будь ласка, name")
        super().__init__(value)

class Phone(Field):
    @Field.value.setter
    def value(self, value):
        self.validate(value)
        super(Phone, Phone).value.__set__(self, value)

    def validate(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError('Телефон має складатися лише з 10 цифр!')    
    

class Record:
    def __init__(self, name, phone_numbers=None, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday) if birthday else None   
        if phone_numbers:
            for phone_number in phone_numbers:
                self.add_phone(phone_number)
    
    def __str__(self):
        result = f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        if self.birthday:            
            result += f", birthday: {self.birthday.value}, days to birthday: {self.days_to_birthday()}"            
        return result   
         
    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        phone.validate(phone_number)
        if phone not in self.phones:
            self.phones.append(phone)

    def find_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def edit_phone(self, old_phone, new_phone):
        phone_replaced = False
        for phone in self.phones:
            if phone.value == old_phone:
                self.remove_phone(old_phone)
                self.add_phone(new_phone)
                phone_replaced = True
                break  # Завершуємо цикл, якщо знайшли телефон
        if not phone_replaced:
            raise ValueError('Номеру телефону не існує')

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                break  # Завершуємо цикл, якщо знайшли телефон
    
    def days_to_birthday(self):
        if self.birthday:
            today = datetime.now().date()
            next_birthday = datetime(today.year, self.birthday._Birthday__value.month, self.birthday._Birthday__value.day).date()
            if today > next_birthday:
                next_birthday = datetime(today.year + 1, self.birthday._Birthday__value.month, self.birthday._Birthday__value.day).date()
            days_to_birthday = (next_birthday - today).days
            return days_to_birthday
        else:
            return None          
     
          
       
class Birthday(Field):
    
    def __init__(self, value):
        super().__init__(value)
        self.value = value

    @Field.value.setter
    def value(self, value):
        try:
            self.__value = datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError('Некоректний формат дня народження (очікується YYYY-MM-DD)!')
        super(Birthday, Birthday).value.__set__(self, value)

    def __str__(self):
        return str(self.__value)

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def iterator(self, item_number):
        counter = 0
        result = ''
        for item, record in self.data.items():
            result += f'{item}: {record}'
            counter += 1
            if counter >= item_number:
                yield result
                counter = 0
                result = ''
