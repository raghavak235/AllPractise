from Item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
    # Run Validations to the received arguments
        assert broken_phones > 0

        self.broken_phones = broken_phones
