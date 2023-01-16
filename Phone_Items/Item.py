import csv

# OOPS Principles
# Encapsulation: Restricting direct access to some attributes.(name and price)
# Abstraction: hiding unnecessary details from the user (Private methods)
# Inheritance: Allows us to reuse the code across the classes
# Polymorphism: refers to many forms, takes input and returns the result accordingly


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):

        # Run Validations to the received arguments
        assert price >= 0
        assert quantity >= 0

        #  Assigning to the object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)
        pass

    # Read only variable
    @property
    def name(self):
        print('You are in the value getter')
        return self.__name

    # Read only variable
    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value


    @name.setter
    def name(self, value):
        if len(value)>10:
            raise Exception('Name is too long')
        print('You are in the name setter')
        self.__name = value



    def calculate_total_price(self):
        return self.__price * self.quantity

    def __connect(self):
        pass

    def send_email(self):
        self.__connect()



    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"
