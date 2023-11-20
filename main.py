from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Введіть, будь ласка, name")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)

    def validate(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError('Телефон має складатися лише з 10 цифр!')

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

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


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]



#========Внутрішня перевірка=======

# Створення нової адресної книги
book = AddressBook()
# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
# Додавання запису John до адресної книги
book.add_record(john_record)
# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)
# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)
# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555
# Видалення запису Jane
book.delete("Jane")
