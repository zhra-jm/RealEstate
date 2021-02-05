class BaseProperty:
    def __init__(self, area, room_numbers, parking, address, **kwargs):
        super().__init__(**kwargs)
        self.area = area
        self.room_numbers = room_numbers
        self.parking = parking
        self.address = address

    @classmethod
    def prompt(cls):
        area = input("Please enter the are: ")
        room_numbers = input("Please enter the number of rooms: ")
        parking = input("Please enter the availability of parking: ")
        address = input("Please enter the address")
        result = {
            'area': area,
            'room_numbers': room_numbers,
            'parking': parking,
            'address': address
        }
        return result


class Apartment(BaseProperty):
    def __init__(self, floor, elevator, balcony, **kwargs):
        super().__init__(**kwargs)
        self.floor = floor
        self.elevator = elevator
        self.balcony = balcony

    @classmethod
    def prompt(cls):
        floor = input("Please enter the floor level: ")
        elevator = input("Please enter the availability of elevator: ")
        balcony = input("Please enter the availability of balcony: ")
        result = {
            'floor': floor,
            'elevator': elevator,
            'balcony': balcony,
        }
        result.update(BaseProperty.prompt())
        return result


class House(BaseProperty):
    def __init__(self, pool, yard, **kwargs):
        super().__init__(**kwargs)
        self.pool = pool
        self.yard = yard

    @classmethod
    def prompt(cls):
        pool = input("Please enter the availability of pool: ")
        yard = input("Please enter yard: ")
        result = {
            'pool': pool,
            'yard': yard
        }
        result.update(BaseProperty.prompt())
        return result


class Rental:
    def __init__(self, pre_paid, monthly, **kwargs):
        super().__init__(**kwargs)
        self.pre_paid = pre_paid
        self.monthly = monthly

    @classmethod
    def prompt(cls):
        pre_paid = input("please enter ur pre paid amount: ")
        monthly = input("Please enter ur monthly amount: ")
        result = {'pre_paid': pre_paid, 'monthly': monthly}
        return result


class Purchasable:
    def __init__(self, cost, **kwargs):
        super().__init__(**kwargs)
        self.cost = cost

    @classmethod
    def prompt(cls):
        return {'cost': input("please enter the amount of ur cost: ")}





















