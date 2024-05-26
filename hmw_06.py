import re
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if self.validate(value):
            super().__init__(value)
        else:
            raise ValueError(f"Invalid phone number: {value}")

    @staticmethod
    def validate(value):
        pattern = re.compile(r'^\d{10}$')
        return bool(pattern.match(value))

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

   def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError(f"Old phone number {old_phone} not found.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        phones = ', '.join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())


# Using example
if __name__ == "__main__":
    
    book = AddressBook()

    
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    print("All records in the address book:")
    for name, record in book.data.items():
        print(record)

    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print("\nAfter editing John's phone:")
    print(john)

    found_phone = john.find_phone("5555555555")
    print(f"\nFound phone in John's record: {john.name}: {found_phone}")  # Виведення: John: True

    book.delete("Jane")
    print("\nAfter deleting Jane's record:")
    print(book)
