from item import Item
class Phone(Item):
    pay_rate = .5
    def __init__(self, name: str, price: float, quantity=0, broken_phone=0):
        # Call to super function to have access to all attributes/methods
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received arguments
        assert broken_phone >= 0, f"Broken phone {broken_phone} is not greater or equal to zero"

        # Assign to self object
        self.broken_phones = broken_phone
